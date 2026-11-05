# Tools

Automation helpers for Fluxpoint.

## Setup

On Arch Linux:

```bash
./tools/setup_dev.sh
```

The script installs KiCad, FreeCAD, OpenSCAD, ARM GCC, probe-rs, OpenOCD, sigrok-cli, and Python test dependencies. It prints the MCP configuration snippet; it does not edit your OpenCode config.

## Requirements

Python 3.10+.

- `check-docs` and `check-config` need `pyyaml` for config checks.
- `flash` needs only the standard library.
- `serial` needs `pyserial`.
- `logic` needs `sigrok-cli` (Arch: `pacman -S sigrok-cli`).
- `power` needs `pyvisa` and a SCPI-capable instrument.

```bash
python -m pip install -r tools/requirements.txt
```

## Commands

```bash
# Markdown link validation
python tools/fluxpoint_cli.py check-docs

# YAML validation
python tools/fluxpoint_cli.py check-config

# Copy a UF2 to a bootloader mount
python tools/fluxpoint_cli.py flash --uf2 build/left/zephyr/zmk.uf2 --mount /media/$USER/NICENANO

# Auto-detect a nice!nano bootloader volume
python tools/fluxpoint_cli.py flash --uf2 build/left/zephyr/zmk.uf2 --label nicenano

# Serial console log
python tools/fluxpoint_cli.py serial --port /dev/ttyACM0 --baud 115200 --log serial.log

# Logic analyzer capture (sigrok-cli)
python tools/fluxpoint_cli.py logic --driver fx2lafw --channels D0,D1 --time 2s --output trackpoint.sr

# Optional SCPI measurement
python tools/fluxpoint_cli.py power --resource USB0::0x1234::0x5678::INSTR --measure current
```

## Tests

```bash
python -m pytest -q tools/tests
```

## Design notes

- The CLI imports hardware libraries lazily, so documentation/config checks work on a machine without a logic analyzer or serial port.
- `check-docs` ignores external URLs, anchors, and links inside code fences/inline code.
- `flash` does not format or unmount the volume; it copies the UF2 and relies on the bootloader to reboot.
- `logic` is a thin wrapper around `sigrok-cli`; use PulseView for interactive decoding.
- No script writes to the PCB or firmware without an explicit path/argument.
