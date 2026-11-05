---
name: kicad
description: Use when working on Fluxpoint KiCad schematics or PCBs, Konnect/KiCAD MCP workflows, ERC/DRC, footprints, BOM, Gerber/drill export, or design reviews.
---

# KiCad workflow

Read `docs/architecture.md`, `docs/requirements.md`, `hardware/pcb/README.md`, and the relevant ADRs before editing.

## Project constraints

- Two mirrored boards, 1.6 mm, 2 layers, JLCPCB; hand assembly.
- nice!nano clone socketed with 2.54 mm headers; controller at the top edge, outside keycaps.
- 42-key matrix, Choc V1 hot-swap, 1N4148W SOD-123, col2row.
- Right half: TrackPoint 4-pin FPC 0.5 mm, OLED I2C, future fingerprint UART header + load switch.
- Left half: simpler; no TrackPoint/fingerprint.
- 502030 battery connector, power switch, battery ADC.
- Antenna keepout; no battery/magnet directly over the antenna.
- Target 15–16 mm; confirm the stack-up before final layout.

## Workflow

1. Read the pin budget in `docs/architecture.md` §5; do not guess pins.
2. Create/update the schematic; run ERC.
3. Assign footprints; check connector orientation and FPC contact side.
4. Lay out the board; run DRC with the project rules.
5. Export Gerber, drill, BOM, and pick-and-place; inspect the fabrication package.
6. Record unresolved issues in the PR/ADR.

## Konnect/KiCad MCP

- Konnect is the primary KiCad 10 MCP; see `docs/automation.md`.
- Konnect is AGPL-3.0 in the archived repo; Konnect-EDA is the successor and free for hobby/open-hardware work, commercial for businesses.
- Fallback: `KiCAD-MCP-Server` (MIT).
- Never trust an automated ERC/DRC pass without reviewing the report.
- Never fabricate a board from AI-generated changes without a human review.

## Commands

```bash
kicad-cli sch erc --output erc.rpt board.kicad_sch
kicad-cli pcb drc --output drc.rpt board.kicad_pcb
kicad-cli pcb export gerbers --output gerbers/ board.kicad_pcb
kicad-cli pcb export drill --output drill/ board.kicad_pcb
```

## Safety

- Verify battery polarity, charger, and backfeed protection.
- Verify TrackPoint VCC (3.3 V assumed, not 5 V).
- Verify no VBUS path between halves.
- Verify antenna keepout and RF ground.
- Human sign-off before ordering.
