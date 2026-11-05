---
name: bringup
description: Use when testing Fluxpoint hardware on the bench, characterizing the nice!nano clone, debugging the TrackPoint, capturing PS/2/UART with a logic analyzer, measuring power/BLE, or running acceptance tests.
---

# Bring-up workflow

Read `docs/bringup.md`, `docs/pinmap.md`, `docs/bench-log.md`, `docs/trackpoint.md`, `docs/requirements.md` §5, and `docs/bom.md`.

## Safety

- Protected LiPo only; verify polarity; never charge unattended.
- Current-limit the bench supply: 100 mA first power-up, 300 mA for TrackPoint/fingerprint. If no current-limited supply is available, borrow one before first power-up.
- Disconnect power before rewiring.
- Treat the TrackPoint flex as fragile; support the stiffener; do not pull the flex.
- ESD precautions around the controller and TrackPoint.

## Phase 1 order

1. nice!nano clone: shorts, 3.3 V, charger, UF2, pinout.
2. Matrix: 4x6, 1N4148, col2row, all keys; flash `fluxpoint_bench_left/right`.
3. OLED: I2C 0x3C, display, blank.
4. TrackPoint: continuity, 3.3 V current, logic capture, PS/2 decode, driver, reset.
5. Power/BLE: active/deep-sleep current, range, USB/BLE hosts.

Record every measurement in `docs/bench-log.md`. Do not mark a criterion passed from a multimeter average when it needs a scope; mark it pending and record the instrument gap.

## TrackPoint specifics

- 4-pin 0.5 mm FPC; breakout with top/bottom footprints.
- Likely PS/2: VCC/GND/CLK/DATA; confirm, do not assume 5 V.
- Try `0xFF`, RC reset, MOSFET power-cycle, GPIO driver, alternate baud.
- Fallback to a known PS/2 module if needed.

## Commands

```bash
python tools/fluxpoint_cli.py serial --port /dev/ttyACM0 --baud 115200 --log serial.log
python tools/fluxpoint_cli.py logic --driver fx2lafw --channels D0,D1 --time 2s --output tp.sr
python tools/fluxpoint_cli.py power --resource USB0::0x1234::0x5678::INSTR --measure current
```

## Acceptance

Use the checklist in `docs/bringup.md` §4. Record measured values, not just pass/fail. Do not mark a test passed without a measurement or observation.

## Escalation

If a test fails, document the symptom, wiring, firmware revision, and measurement. Do not change multiple variables at once.
