#!/usr/bin/env python3
"""Fluxpoint automation CLI.

Dependency-free commands: check-docs, check-config, flash.
Optional hardware commands: serial (pyserial), logic (sigrok-cli), power (pyvisa).
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

VERSION = "0.1.0"
DEFAULT_ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
SKIP_DIRS = {".git", "build", "node_modules", ".venv", "venv", "__pycache__", "zephyr", "modules", "zmk", "optional"}
SKIP_ZMK_WORKSPACE = {"zmk", "zephyr", "modules", "optional", "tools", ".west"}


def is_skipped(path: Path, root: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return True
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    if len(rel.parts) >= 3 and rel.parts[0] == "firmware" and rel.parts[1] == "zmk-config":
        return rel.parts[2] in SKIP_ZMK_WORKSPACE
    return False


def iter_markdown(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if is_skipped(path, root):
            continue
        yield path


def strip_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))


def is_external(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:"))
        or lowered.startswith("#")
        or lowered.startswith("//")
    )


def normalize_target(target: str) -> str:
    # Drop anchors and query strings; decode simple %20-style escapes.
    target = target.split("#", 1)[0].split("?", 1)[0]
    try:
        from urllib.parse import unquote

        return unquote(target)
    except Exception:
        return target


def find_broken_links(root: Path) -> List[Tuple[Path, str]]:
    broken: List[Tuple[Path, str]] = []
    for md in iter_markdown(root):
        text = strip_code(md.read_text(encoding="utf-8", errors="replace"))
        for raw in LINK_RE.findall(text):
            if is_external(raw):
                continue
            target = normalize_target(raw)
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            if not candidate.exists():
                broken.append((md.relative_to(root), raw))
    return broken


def check_docs(root: Path) -> int:
    broken = find_broken_links(root)
    if not broken:
        print(f"OK: all local Markdown links resolve under {root}")
        return 0
    for source, target in broken:
        print(f"BROKEN: {source} -> {target}")
    print(f"\n{len(broken)} broken link(s)")
    return 1


def check_config(root: Path) -> int:
    try:
        import yaml  # type: ignore
    except ImportError:
        print("ERROR: PyYAML is required for check-config (pip install pyyaml)", file=sys.stderr)
        return 2

    failures = 0
    checked = 0
    for suffix in ("*.yml", "*.yaml"):
        for path in sorted(root.rglob(suffix)):
            if is_skipped(path, root):
                continue
            checked += 1
            try:
                yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001 - report the file and move on
                failures += 1
                print(f"INVALID: {path.relative_to(root)}: {exc}")
    if failures:
        print(f"\n{failures} invalid YAML file(s) out of {checked}")
        return 1
    print(f"OK: {checked} YAML file(s) parsed")
    return 0


def candidate_mounts() -> List[Path]:
    user = os.environ.get("USER", "")
    roots = [
        Path("/media") / user,
        Path("/run/media") / user,
        Path("/Volumes"),
        Path("/mnt"),
    ]
    found: List[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for child in root.iterdir():
            if child.is_dir():
                found.append(child)
    return found


def find_uf2_mount(labels: Sequence[str]) -> Optional[Path]:
    wanted = {label.lower() for label in labels}
    for mount in candidate_mounts():
        name = mount.name.lower()
        if name in wanted or any(label in name for label in wanted):
            return mount
    return None


def flash_uf2(uf2: Path, mount: Optional[Path] = None, labels: Sequence[str] = ("nicenano", "nice_nano", "nrf52840")) -> int:
    if not uf2.exists():
        print(f"ERROR: UF2 file not found: {uf2}", file=sys.stderr)
        return 2
    if mount is None:
        mount = find_uf2_mount(labels)
    if mount is None:
        print("ERROR: bootloader mount not found. Pass --mount or double-tap reset.", file=sys.stderr)
        return 2
    if not mount.is_dir():
        print(f"ERROR: mount is not a directory: {mount}", file=sys.stderr)
        return 2
    destination = mount / uf2.name
    print(f"Copying {uf2} -> {destination}")
    shutil.copy2(uf2, destination)
    print("Copy complete; the controller should reboot.")
    return 0


def serial_log(port: str, baud: int = 115200, log: Optional[Path] = None) -> int:
    try:
        import serial  # type: ignore
    except ImportError:
        print("ERROR: pyserial is required for serial (pip install pyserial)", file=sys.stderr)
        return 2

    log_handle = log.open("a", encoding="utf-8") if log else None
    print(f"Opening {port} at {baud} baud; Ctrl+C to stop.")
    try:
        with serial.Serial(port, baud, timeout=1) as conn:
            while True:
                line = conn.readline()
                if not line:
                    continue
                text = line.decode("utf-8", errors="replace").rstrip()
                print(text)
                if log_handle:
                    log_handle.write(text + "\n")
                    log_handle.flush()
    except KeyboardInterrupt:
        print("\nStopped.")
        return 0
    except Exception as exc:  # noqa: BLE001 - hardware errors are expected
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    finally:
        if log_handle:
            log_handle.close()


def logic_capture(driver: str, channels: Optional[str], duration: str, output: Path, decoder: Optional[str]) -> int:
    cmd = ["sigrok-cli", "-d", driver, "--time", duration, "-o", str(output)]
    if channels:
        cmd += ["-C", channels]
    if decoder:
        cmd += ["-P", decoder]
    print("Running:", " ".join(cmd))
    try:
        return subprocess.run(cmd, check=False).returncode
    except FileNotFoundError:
        print("ERROR: sigrok-cli not found (pacman -S sigrok-cli)", file=sys.stderr)
        return 2


def power_measure(resource: str, measure: str) -> int:
    try:
        import pyvisa  # type: ignore
    except ImportError:
        print("ERROR: pyvisa is required for power (pip install pyvisa)", file=sys.stderr)
        return 2

    command = "MEAS:CURR?" if measure == "current" else "MEAS:VOLT?"
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource(resource)
    try:
        value = inst.query(command).strip()
        print(f"{measure}: {value}")
        return 0
    finally:
        inst.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fluxpoint automation CLI")
    parser.add_argument("--version", action="version", version=f"fluxpoint {VERSION}")
    sub = parser.add_subparsers(dest="command", required=True)

    docs = sub.add_parser("check-docs", help="validate local Markdown links")
    docs.add_argument("--root", type=Path, default=DEFAULT_ROOT)

    config = sub.add_parser("check-config", help="parse all YAML files")
    config.add_argument("--root", type=Path, default=DEFAULT_ROOT)

    flash = sub.add_parser("flash", help="copy a UF2 to a bootloader mount")
    flash.add_argument("--uf2", type=Path, required=True)
    flash.add_argument("--mount", type=Path, default=None)
    flash.add_argument("--label", action="append", default=None, help="mount label to search (repeatable)")

    serial_cmd = sub.add_parser("serial", help="log a serial console")
    serial_cmd.add_argument("--port", required=True)
    serial_cmd.add_argument("--baud", type=int, default=115200)
    serial_cmd.add_argument("--log", type=Path, default=None)

    logic = sub.add_parser("logic", help="capture with sigrok-cli")
    logic.add_argument("--driver", required=True)
    logic.add_argument("--channels", default=None)
    logic.add_argument("--time", default="2s")
    logic.add_argument("--output", type=Path, default=Path("capture.sr"))
    logic.add_argument("--decoder", default=None)

    power = sub.add_parser("power", help="read a SCPI measurement")
    power.add_argument("--resource", required=True)
    power.add_argument("--measure", choices=("current", "voltage"), default="current")

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "check-docs":
        return check_docs(args.root)
    if args.command == "check-config":
        return check_config(args.root)
    if args.command == "flash":
        labels = tuple(args.label) if args.label else ("nicenano", "nice_nano", "nrf52840")
        return flash_uf2(args.uf2, args.mount, labels)
    if args.command == "serial":
        return serial_log(args.port, args.baud, args.log)
    if args.command == "logic":
        return logic_capture(args.driver, args.channels, args.time, args.output, args.decoder)
    if args.command == "power":
        return power_measure(args.resource, args.measure)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
