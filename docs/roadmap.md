# Roadmap

- **Status:** Phase 0 baseline
- **Last updated:** 2026-11-05
- **Related:** [Requirements](requirements.md), [Architecture](architecture.md), [Feasibility](feasibility.md)

This roadmap is milestone-based. A phase is complete only when its exit criteria are met; dates are intentionally omitted.

## Phase overview

| Phase | Goal | Main output | Exit criteria |
|---|---|---|---|
| 0 | Close the skeleton and tooling | Docs, ADRs, BOM, automation, CI, skills, baseline firmware | Docs reviewed; CI green; BOM ready; repository public |
| 1 | Prove the risky parts on the bench | Breadboard matrix, TrackPoint, OLED, power, BLE measurements | TrackPoint works or fallback chosen; matrix/OLED proven; power budget measured |
| 2 | Build the first integrated prototype | PCB v0.1, case v0.1, firmware v0.1 | All keys, TrackPoint, OLED, BLE, USB, battery, and case fit work |
| 3 | Harden and release | PCB/case final, acceptance tests, release package | All acceptance criteria met; fabrication files and firmware released |
| 4 | Build the configurator app | Flutter MVP and advanced settings | Keymap editing and import/export work on Android/desktop |
| 5 | Add optional capabilities | Dongle, fingerprint/FIDO2, wired split | Each optional feature has its own ADR and acceptance test |

## Phase 0 — Skeleton and tooling

**Deliverables**

- Requirements, architecture, roadmap, feasibility, BOM, bring-up, TrackPoint, and layout docs.
- ADRs for all agreed decisions.
- Public repository, licenses, NOTICE, and attribution.
- Architecture and connectivity diagrams.
- Automation CLI: docs/config checks, flash, serial, logic capture, power helpers.
- GitHub Actions: documentation/tool checks and baseline ZMK firmware build.
- Project skills for KiCad, ZMK, CAD, bring-up, BOM, and docs.
- Baseline ZMK Corne configuration for tooling validation.

**Exit criteria**

- `python tools/fluxpoint_cli.py check-docs` passes.
- `python tools/fluxpoint_cli.py check-config` passes.
- `python -m pytest -q tools/tests` passes.
- Baseline firmware workflow builds left, right, and settings-reset UF2 files.
- BOM includes owned and missing parts with suppliers and estimates.
- TrackPoint breakout requirements and test procedure are documented.

**Dependencies**

- User supplies TrackPoint close-ups/measurements (pitch confirmed 0.5 mm; contact side still open).
- User confirms the exact nice!nano clone variant and pinout in Phase 1.

## Phase 1 — Bench characterization and breadboard

**Deliverables**

- nice!nano clone characterization: pinout, charger, 3.3 V rail, current, UF2 flashing.
- Breadboard matrix with 4x6 wiring and ZMK baseline firmware.
- TrackPoint breakout PCB: 4-pin FPC 0.5 mm top/bottom footprints, header, pull-ups, reset/MOSFET options.
- TrackPoint test: continuity, 3.3 V current, logic capture, PS/2 driver, reset strategy.
- OLED test: I2C address, display widgets, blank behavior.
- Power/BLE measurements: battery, charging, deep sleep, range, antenna keepout.
- Decision on known-module fallback if the Dell module cannot be used.

**Exit criteria**

- All 42 matrix positions register on the breadboard.
- OLED initializes and blanks correctly.
- TrackPoint responds to movement and clicks, or the fallback module is ordered.
- BLE split works between two nice!nano boards at ≥5 m.
- Battery current and deep-sleep current are measured and consistent with the autonomy target.
- The final pin map and TrackPoint wiring are agreed.

**Risks**

- TrackPoint is not PS/2 or needs an inaccessible reset.
- The FPC contact side/pitch is wrong.
- The nice!nano clone has a different pinout or charger behavior.
- The logic analyzer is not available or the PS/2 decoding is inconclusive.

## Phase 2 — PCB v0.1, case v0.1, firmware v0.1

**Deliverables**

- Schematic and PCB layout for left and right halves.
- Two mirrored PCBs, 1.6 mm, 2 layers, JLCPCB fabrication.
- FR4 switch plates, 1.2–1.6 mm.
- 3D-printed case v0.1: battery pocket, magnet pockets, OLED window, TrackPoint bracket, USB-C/reset/switch access.
- ZMK custom shield: matrix, TrackPoint, OLED, ZMK Studio, 10-second display behavior.
- Bring-up of PCB v0.1 and case v0.1.
- First BOM revision with actual part numbers.

**Exit criteria**

- All keys register on the PCB.
- TrackPoint works on the PCB with the chosen reset strategy.
- OLED wakes for 10 seconds and blanks.
- BLE split, USB HID, and BLE HID work.
- Battery charges and reports level.
- Case fits the PCB, battery, magnets, and TrackPoint; height ≤16 mm.
- No shorts, no VBUS backfeed, no obvious RF degradation.

**Risks**

- PCB footprint or pin-mapping errors.
- TrackPoint flex/connector damage during assembly.
- Case tolerances and magnet alignment.
- Antenna detuning from battery/magnets.
- ZMK driver/fork incompatibility.

## Phase 3 — Final hardware and acceptance

**Deliverables**

- PCB v0.2 or v1.0 with fixes.
- Final case revision and plate.
- Final firmware and release UF2s.
- Acceptance test report.
- Final BOM, fabrication files, and assembly notes.
- Public release with licenses and attribution.

**Exit criteria**

- All criteria in [Requirements §5](requirements.md#5-acceptance-criteria) pass.
- Height, weight, autonomy, latency, range, and magnetic hold measured.
- TrackPoint drift and reset behavior verified over multiple power cycles.
- ZMK Studio keymap editing verified over USB and BLE.
- Case and mount survive travel/handling tests.
- Release artifacts reproducible from the repository.

## Phase 4 — Flutter configurator

**Deliverables**

- Flutter app in `software/configurator`.
- Android, Linux, Windows, and macOS builds.
- ZMK Studio protocol client over USB serial and BLE GATT.
- Keymap/layer editor, keycodes/behaviors, import/export, local profiles.
- Advanced settings via custom RPC: TrackPoint sensitivity/scroll, display timeout, power behavior.
- BLE profile management, DFU/firmware update, diagnostics/logs.
- CI for analyze/test/build.

**Exit criteria**

- App connects to the keyboard over USB and BLE.
- Keymap edits persist and survive reconnect.
- Import/export round-trips.
- Advanced settings are documented and safe.
- App builds for all target platforms.

**Risks**

- ZMK Studio protocol changes.
- Custom RPC compatibility with ZMK versions.
- BLE permissions/limits on Android/desktop.
- DFU implementation complexity.

## Phase 5 — Optional capabilities

| Capability | Notes | Gate |
|---|---|---|
| Dongle | ZMK central with no keys; improves battery/connection stability | Phase 3 stable; dongle ADR |
| Fingerprint | HLK-ZW0905 over UART; expansion header already reserved | TrackPoint/display stable; privacy/threat model |
| FIDO2/CTAP2 | Separate security MCU or certified key; secure element assessment | Security ADR; legal/compliance review |
| Wired split | Full-duplex UART, 4-wire protected link | ZMK wired split maturity; protection review |

## Cross-phase risks

| Risk | Mitigation |
|---|---|
| TrackPoint protocol/reset | Breadboard test, logic analyzer, RC/MOSFET, known-module fallback |
| Antenna/RF | Battery offset, keepout, range test, case material check |
| Low-profile height | Measure stack-up, print test coupons, local battery pocket |
| Magnet hold/flatness | Pull-force test, steel-plate recess, feet |
| ZMK Studio limitations | Document limits; custom RPC for advanced settings |
| Supply/import delays | Order long-lead parts in Phase 0/1; local alternatives |
| Budget | Track BOM; hand assembly; borrow 3D printer |
| Documentation drift | ADRs + link/config checks in CI |

## Decision gates

1. **TrackPoint gate (Phase 1):** use the Dell module or switch to a known PS/2 module.
2. **Pin-map gate (Phase 1):** freeze matrix, TrackPoint, display, battery, and expansion pins before schematic.
3. **RF gate (Phase 2):** battery/magnet/case combination must meet range target before final PCB.
4. **Height gate (Phase 2):** assembled stack must be ≤16 mm before final case.
5. **App gate (Phase 3):** ZMK Studio keymap editing must work before the Flutter app scope expands.
