---
name: fluxpoint
description: Use for any Fluxpoint project work, including status, decisions, repository conventions, documentation, build/test commands, and coordination across hardware, firmware, software, and tools.
---

# Fluxpoint

Fluxpoint is a low-profile Corne 3x6+3 split keyboard with a salvaged Dell TrackPoint, BLE split, USB/BLE host, SSD1306 OLED, 502030 battery per half, and a magnetic N52/steel-plate/ball-head mount. The final firmware is right-central because the TrackPoint is on the right half.

## Current phase

Phase 0: documentation, ADRs, automation, CI, skills, and a baseline Corne ZMK config. No custom PCB or case yet.

## Key decisions

- 42 keys, Choc V1 hot-swap, 1N4148W SOD-123.
- Socketed Tenstar/SuperMini nice!nano v2 clone.
- ZMK + modules; ZMK Studio enabled from v1.
- BLE split + USB/BLE host; no wired split or dongle in v1.
- TrackPoint on the right thumb cluster; right half central.
- OLED off by default, 10-second wake; nice!view footprint in the final PCB.
- 502030 250 mAh per half; 15–16 mm target.
- 3D-printed case + FR4 plate; MBK blank keycaps.
- 4x N52 magnets + 1 mm steel plate + 1/4"-20 ball head.
- Flutter configurator is Phase 3, not v1.
- FIDO2/fingerprint deferred; expansion header reserved.

## Repository map

- `docs/` — requirements, architecture, roadmap, feasibility, BOM, bring-up, TrackPoint, layout, ADRs.
- `hardware/` — PCB, case, diagrams, TrackPoint notes.
- `firmware/` — ZMK config, modules, dongle.
- `software/configurator/` — Flutter app plan.
- `tools/` — automation CLI and tests.
- `.opencode/skills/` — project skills.

## Commands

```bash
python tools/fluxpoint_cli.py check-docs
python tools/fluxpoint_cli.py check-config
python -m pytest -q tools/tests
```

Firmware baseline build is documented in `docs/automation.md`.

## Rules

- Documentation and code identifiers are English.
- Architecture/scope/interface changes need an ADR in `docs/decisions/`.
- Keep Corne attribution and licenses intact.
- Do not commit generated fabrication files, UF2, STL, or build outputs.
- Human review is required for schematics, PCBs, safety, and releases.
- Do not purchase parts automatically; update `docs/bom.md` and ask.
