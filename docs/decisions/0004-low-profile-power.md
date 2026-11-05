# ADR 0004: Low-profile stack, battery, and case

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [Requirements](../requirements.md), [BOM](../bom.md)

## Context

The keyboard should be as low-profile as possible. Choc V1 switches and MBK keycaps set the key-area height; hot-swap sockets add ~1.5 mm below the PCB. The controller is socketed to be replaceable. A 502030 cell is 5 mm thick and is the largest practical battery under the controller footprint. The battery and magnets can affect the antenna.

## Decision

- Kailh Choc V1 hot-swap sockets; 1N4148W SOD-123 diodes.
- 1.6 mm PCB; 1.2–1.6 mm FR4 switch plate.
- Socketed nice!nano at the top edge, outside the keycap field.
- 502030 250 mAh protected LiPo per half, in a local pocket under the controller.
- 3D-printed case with a 3–5 mm bottom; target 15–16 mm at the keycaps.
- USB-C charging on each half; physical on/off switch; battery ADC.
- Antenna keepout and battery offset; BLE range is measured with the battery and magnets installed.

## Consequences

- The key area stays close to commercial Choc Corne height while keeping a serviceable controller.
- The case bottom is not uniform; the battery pocket and feet must be designed together so the keyboard sits flat.
- The controller socket does not force the key area height, but it must be below the keycaps at the top edge.
- Battery capacity/autonomy and RF range must be verified, not assumed.
- The 250 mAh cell and ≥2 week target imply an average current of ≈0.75 mA; TrackPoint idle current is the largest unknown and may require a load switch or duty-cycle policy.
