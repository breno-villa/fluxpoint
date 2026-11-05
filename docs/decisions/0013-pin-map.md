# ADR 0013: Pin map and board-level interfaces

- **Status:** Proposed
- **Date:** 2026-11-05
- **Related:** [Pin map](../pinmap.md), [Architecture](../architecture.md), [Requirements](../requirements.md), [Bring-up](../bringup.md), [ADR 0002](0002-mcu-firmware-base.md), [ADR 0003](0003-connectivity.md), [ADR 0005](0005-trackpoint.md), [ADR 0006](0006-display.md)

## Context

The Phase 2 schematic cannot start until the matrix, TrackPoint, display, battery ADC, and expansion pins are fixed. The current map is a feasibility estimate built from the stock Corne shield and the documented nice!nano v2 board definition. The Tenstar/SuperMini clone may differ in pad labels, exposed GPIO count, charger behavior, or battery ADC topology.

The design also has a tight pin budget:

- the Pro Micro header exposes 18 GPIO on the documented nice!nano v2;
- the v1 keyboard needs 16–17 pins including the shared display header and an optional TrackPoint reset/load switch;
- the future fingerprint header adds 3 pins, which may exceed 18 unless extra pads, NFC pins, a shared load switch, or an expander are used.

The display header must support both an I2C SSD1306 OLED (v1) and a 3-wire SPI nice!view (alternative) without populating both.

## Decision

- Adopt the candidate map in [Pin map](../pinmap.md) as the working map for the Phase 1 `fluxpoint_bench_left/right` shield.
- Verify every function on the clone before the Phase 2 schematic.
- Freeze the map at the Phase 1 pin-map gate and copy the frozen values into the Phase 2 schematic notes.
- Keep the right half central in v1; the TrackPoint stays on the central side.
- Use D0/D1 as the preferred TrackPoint UART pins and D2/D3 as the shared display I2C/SPI clock/data pins.
- Reserve D8/D9 for display CS, TrackPoint reset, or a TrackPoint load switch; resolve the exact assignment at the gate.
- Do not use the NFC pins P0.09/P0.10 unless they are explicitly enabled as GPIO and the pin budget requires them.
- Treat the future fingerprint header as reserved but unpopulated; if the final budget does not fit, document the limitation and revise the expansion plan rather than compromising v1.

## Consequences

- The Phase 1 bench shield and the Phase 2 schematic share one candidate map, so bring-up results transfer directly.
- The pin map is not final until the gate; firmware and hardware must not treat the candidate table as frozen.
- The 18-GPIO header budget is tight. The fingerprint expansion may require NFC pins, a shared load switch, an I2C expander, or a later board revision.
- The shared display header must be checked for both I2C and SPI pin remapping before layout.
- The battery ADC topology must be measured; if the clone needs a divider pin, the budget loses one more GPIO.
- Any post-gate change requires a new ADR or a superseding update to this record.

## Gate evidence

The ADR moves to **Accepted** only when [Bench log](../bench-log.md) records:

- matrix rows/columns verified on both halves;
- OLED at `0x3C` on the chosen I2C pins;
- TrackPoint CLK/DATA captured and decoded;
- reset/load-switch pin verified if used;
- battery ADC reading checked against a multimeter;
- shared display header checked for I2C and SPI compatibility;
- no conflict with SWD, USB, reset, LED, charger, or NFC.
