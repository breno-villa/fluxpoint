# Hardware

This directory contains the electrical and mechanical design files for Fluxpoint. No PCB or case is frozen yet; Phase 2 produces the first integrated prototype.

## Structure

| Path | Contents |
|---|---|
| `pcb/` | KiCad projects for left and right halves (and future dongle) |
| `case/` | FreeCAD/OpenSCAD/STEP files for the case and plates |
| `diagrams/` | Block diagrams, power tree, pinout, matrix, and mounting diagrams |
| `trackpoint/` | Salvaged TrackPoint measurements, connector notes, and bracket data |

## Fixed constraints

- 42 keys, Corne 3x6+3, Choc V1 hot-swap.
- nice!nano v2 clone, socketed, at the top edge outside the keycap field.
- 502030 250 mAh battery per half, USB-C charging, slide switch.
- Right half is central (TrackPoint + OLED); left half is peripheral.
- 0.91" SSD1306 OLED; nice!view footprint in the final PCB.
- 4x N52 magnets + 1 mm steel plate + 1/4"-20 ball head.
- Target 15–16 mm with MBK keycaps; ≤250 g per half.
- Antenna keepout around the controller; no battery/magnet directly over the antenna.

## Design order

1. Measure the nice!nano clone and TrackPoint on the bench (Phase 1).
2. Freeze the pin map and TrackPoint connector.
3. Schematic + ERC.
4. PCB layout + DRC; two mirrored boards.
5. Case/plate v0.1; print and fit.
6. Bring-up and acceptance.

## TODO

- [ ] Pin map and schematic
- [ ] PCB layout (left/right)
- [ ] Case and plate
- [ ] BOM with exact part numbers
- [ ] Bring-up report
- [ ] Fabrication release

## Licenses

Hardware is CERN-OHL-S-2.0. Corne-derived blocks retain their original MIT/CC BY 4.0 notices; see [NOTICE](../NOTICE).
