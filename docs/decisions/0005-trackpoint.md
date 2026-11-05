# ADR 0005: TrackPoint integration

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [TrackPoint](../trackpoint.md), [Bring-up](../bringup.md), [Layout](../layout.md)

## Context

The builder has a salvaged Dell TrackPoint module from a Latitude 0D19TR keyboard. It is a 4-wire FPC device with a 0.5 mm pitch connector, ~13.5 x 10.9 x 3.9 mm, with a black cap. It is likely PS/2, but the protocol and reset behavior are unconfirmed. ZMK has a PS/2 TrackPoint driver module, but it requires a ZMK fork with mouse support and often a power-on-reset. The module has no dedicated buttons, so clicks must come from the keyboard. The 250 mAh cell and the ≥2 week target leave little power headroom for a continuously powered TrackPoint.

## Decision

- Use the salvaged Dell module first.
- Mount it in the right thumb cluster; the cap is operated by the right thumb.
- Provide left/right/middle click from the right thumb cluster, either as dedicated keys or on a pointing layer. The final keymap resolves the exact binding.
- Use a held thumb key for scroll.
- Connect through a breakout with 4-pin 0.5 mm FPC top- and bottom-contact footprints, pull-ups, RC reset, and optional MOSFET power-cycle.
- The right half is central in v1 to keep the TrackPoint on the same side as the host USB and avoid input-split forwarding.
- Measure TrackPoint idle/active current in Phase 1; add a load switch or power policy if it threatens the battery-life target.
- If the module is I2C/analog, damaged, or cannot be reset, fall back to a known PS/2 TrackPoint module with a documented electrical and mechanical adaptation.

## Consequences

- The TrackPoint is validated on a breadboard before the PCB.
- The case needs a bracket with two ears, bottom-grid clearance, and flex strain relief.
- The firmware depends on a pinned ZMK fork/module revision.
- The right-half central role changes the usual USB host port; this is documented.
- The final keymap must resolve how three thumb keys provide base-layer keys, mouse clicks, and scroll.
- TrackPoint power may require a load switch or duty-cycle policy to meet the autonomy target.
