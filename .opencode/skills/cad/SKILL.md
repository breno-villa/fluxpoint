---
name: cad
description: Use when working on the Fluxpoint case, switch plate, magnet pockets, battery pocket, TrackPoint bracket, OLED window, or FreeCAD/OpenSCAD exports.
---

# CAD workflow

Read `hardware/case/README.md`, `docs/architecture.md` §4.7, `hardware/trackpoint/README.md`, and `docs/trackpoint.md` first.

## Dimensions

- 42-key Choc V1, 18 x 17 mm spacing.
- Target 15–16 mm with MBK keycaps; ≤250 g per half.
- 502030 battery: 5 x 20 x 30 mm plus protection/wires.
- TrackPoint: ~13.5 x 10.9 x 3.9 mm; holes ~12.8 mm; black cap; bottom grid must stay clear.
- Magnets: 4x N52 per half, 8x2 or 10x2 mm candidate; steel plate 1 mm.
- Controller: nice!nano clone, 3.2 mm + socket, at top edge outside keycaps.
- OLED: 0.91" 128x32 module; define a window and strain relief.
- USB-C, reset, power switch, battery connector, TrackPoint cap access.

## Rules

- Print a fit coupon for the plate, magnet pockets, TrackPoint bracket, and battery before the full case.
- Keep the antenna keepout: no battery/magnet directly over the controller antenna.
- Design a flat seating plane and feet; the battery pocket must not cause wobble.
- Use heat-set inserts or serviceable screws.
- Add strain relief for the TrackPoint flex.
- Export STEP and STL; do not commit generated artifacts.

## FreeCAD/OpenSCAD MCP

See `docs/automation.md`. FreeCAD must be open with the RPC server running; OpenSCAD MCP uses `uvx openscad-mcp`.

## Checks before printing

- [ ] Bounding box fits the printer.
- [ ] Wall thickness ≥1.2 mm (2 mm preferred).
- [ ] Magnet pockets have 0.1–0.2 mm clearance and correct polarity.
- [ ] Battery pocket has wire clearance and no sharp edges.
- [ ] TrackPoint bottom grid has clearance.
- [ ] OLED window and connector access.
- [ ] USB-C/reset/switch access.
- [ ] Case screws into the PCB/plate without stressing solder joints.
