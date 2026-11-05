# TrackPoint hardware notes

Detailed integration data lives in [docs/trackpoint.md](../../docs/trackpoint.md). This directory is for the physical bracket, breakout files, and measurement photos when they are added.

## Confirmed measurements

| Property | Value |
|---|---|
| Module | Salvaged Dell Latitude 0D19TR TrackPoint |
| PCB size | ~13.5 x 10.9 mm |
| Thickness | ~3.9 mm |
| Mounting holes | ~12.8 mm between centers |
| Flex | 4 conductors |
| Connector | 4-pin FPC, 0.5 mm pitch |
| Cap | Black rubber dome, present |
| Protocol | Likely PS/2; confirm in Phase 1 |

## Breakout plan

- 4-pin FPC 0.5 mm top-contact footprint.
- 4-pin FPC 0.5 mm bottom-contact footprint.
- 4-pin header/JST-SH for VCC/GND/CLK/DATA.
- 4.7 kΩ pull-ups on CLK/DATA.
- RC reset (2x 4.7 kΩ, 100 kΩ, 2.2 µF).
- Optional P-MOSFET power-cycle.
- Test points and 1–10 µF decoupling.

## Bracket plan

- Screw through the two ears (M1.4/M1.6).
- Leave the bottom black sensor grid clear.
- Support the flex with a strain-relief clamp.
- Position in the right thumb cluster; cap accessible to the thumb.

## TODO

- [ ] Confirm contact side (top/bottom).
- [ ] Confirm protocol and reset.
- [ ] Measure current at 3.3 V.
- [ ] Design breakout PCB.
- [ ] Design case bracket.
- [ ] Add close-up photos and original connector reference.
