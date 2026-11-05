# ADR 0005: TrackPoint integration

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [TrackPoint](../trackpoint.md), [Bring-up](../bringup.md), [Layout](../layout.md)

## Context

The builder has a salvaged Dell TrackPoint module from a Latitude 0D19TR keyboard. It is a 4-wire FPC device with a 0.5 mm pitch connector, ~13.5 x 10.9 x 3.9 mm, with a black cap. It is likely PS/2, but the protocol and reset behavior are unconfirmed. ZMK has a PS/2 TrackPoint driver module, but it requires a ZMK fork with mouse support and often a power-on-reset.

## Decision

- Use the salvaged Dell module first.
- Mount it in the right thumb cluster; the cap is operated by the right thumb.
- Use the three right thumb keys for left/right/middle click.
- Use a held thumb key for scroll.
- Connect through a breakout with 4-pin 0.5 mm FPC top- and bottom-contact footprints, pull-ups, RC reset, and optional MOSFET power-cycle.
- The right half is central because the TrackPoint must be on the central side.
- If the module is I2C/analog, damaged, or cannot be reset, fall back to a known PS/2 TrackPoint module.

## Consequences

- The TrackPoint is validated on a breadboard before the PCB.
- The case needs a bracket with two ears, bottom-grid clearance, and flex strain relief.
- The firmware depends on a pinned ZMK fork/module revision.
- The right-half central role changes the usual USB host port; this is documented.
