from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fluxpoint_cli as cli


def test_strip_code_removes_fenced_and_inline() -> None:
    text = "```\n[bad](missing.md)\n```\n`[bad](also-missing.md)`\n[ok](present.md)"
    stripped = cli.strip_code(text)
    assert "missing.md" not in stripped
    assert "also-missing.md" not in stripped
    assert "present.md" in stripped


def test_normalize_target_drops_anchor_and_query() -> None:
    assert cli.normalize_target("page.md#section?x=1") == "page.md"
    assert cli.normalize_target("my%20file.md") == "my file.md"


def test_find_broken_links_detects_missing(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text("[missing](missing.md)\n", encoding="utf-8")
    broken = cli.find_broken_links(tmp_path)
    assert broken == [(Path("docs/a.md"), "missing.md")]


def test_find_broken_links_ignores_external_anchor_and_code(tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text(
        "[web](https://example.com)\n"
        "[anchor](#section)\n"
        "```\n[code](missing.md)\n```\n"
        "`[inline](missing.md)`\n"
        "[ok](a.md)\n",
        encoding="utf-8",
    )
    assert cli.find_broken_links(tmp_path) == []


def test_flash_uf2_copies_file(tmp_path: Path) -> None:
    uf2 = tmp_path / "firmware.uf2"
    uf2.write_bytes(b"UF2")
    mount = tmp_path / "NICENANO"
    mount.mkdir()
    assert cli.flash_uf2(uf2, mount) == 0
    assert (mount / "firmware.uf2").read_bytes() == b"UF2"


def test_flash_uf2_missing_file_returns_error(tmp_path: Path) -> None:
    assert cli.flash_uf2(tmp_path / "missing.uf2", tmp_path) == 2


def test_is_skipped_ignores_west_workspace(tmp_path: Path) -> None:
    workspace = tmp_path / "firmware" / "zmk-config" / "zmk" / "docs"
    workspace.mkdir(parents=True)
    assert cli.is_skipped(workspace / "page.md", tmp_path)
    project_doc = tmp_path / "docs" / "page.md"
    project_doc.parent.mkdir()
    assert not cli.is_skipped(project_doc, tmp_path)


def test_find_uf2_mount(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    mount = tmp_path / "NICENANO"
    mount.mkdir()
    monkeypatch.setattr(cli, "candidate_mounts", lambda: [mount])
    assert cli.find_uf2_mount(["nicenano"]) == mount


def test_check_config_valid_and_invalid(tmp_path: Path) -> None:
    pytest.importorskip("yaml")
    (tmp_path / "valid.yml").write_text("a: 1\n", encoding="utf-8")
    assert cli.check_config(tmp_path) == 0
    (tmp_path / "invalid.yml").write_text("a: [1, 2\n", encoding="utf-8")
    assert cli.check_config(tmp_path) == 1
