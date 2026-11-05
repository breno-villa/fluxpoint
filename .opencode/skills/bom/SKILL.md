---
name: bom
description: Use when updating the Fluxpoint BOM, inventory, procurement notes, supplier choices, cost estimates, or checking which parts are owned or missing.
---

# BOM and procurement

The source of truth is `docs/bom.md`. Read it before recommending a purchase.

## Inventory summary

Owned: 4x nice!nano clone, 100x Choc V1 switches, 100x hot-swap sockets, 100x 1N4148, 100x 1N4148W SOD-123, power switches, OLED, Dell TrackPoint with black cap, breadboard, soldering/multimeter, ST-Link V2, borrowable 3D printer.

Missing: MBK blank keycaps, 2x 502030 250 mAh protected LiPo, 2 PCBs, 2 FR4 plates, 8x N52 magnets, 2 steel plates, 2 ball heads/clamps, screws/standoffs, JST-PH/wire/heatshrink/feet, FPC connectors and breakout adapters, breakout PCB, logic analyzer, filament. The Phase 1 batch is in `docs/bom.md` §8; it was approved on 2026-11-05 but the order has not been placed.

## Supplier strategy

- JLCPCB: PCBs, FR4 plates, breakout.
- AliExpress: keycaps, batteries, magnets, FPC connectors/adapters, logic analyzer.
- Local: screws, wire, filament, ball heads/clamps, steel plates.
- Budget: R$ 500–1,500 target; keyboard parts estimate R$ 770–1,500, tools add R$ 100–200, so the total can exceed the target before shipping. The Phase 1 batch is mostly a subset of that estimate; borrow the bench supply and oscilloscope if possible.

## Rules

- Do not purchase automatically. Update the BOM and ask the user.
- Mark estimates clearly; prices/import taxes change.
- Prefer protected LiPo cells and verified polarity.
- Buy both FPC top/bottom contact variants; pitch is 0.5 mm. A breakout adapter is for the bench; pogo pins/probes are for probing, not a substitute for the ZIF connector.
- Do not add nice!view or fingerprint parts to v1 unless the scope changes via ADR.
- The Phase 1 batch was approved on 2026-11-05; the user places the order.
- Record exact part numbers, supplier links, actual prices, tracking, and receipt in `docs/bom.md` §8, and update the owned inventory in §1.

## Checks

- [ ] Every missing part has quantity, supplier, estimate, and note.
- [ ] Owned parts are not duplicated.
- [ ] Long-lead items are ordered early.
- [ ] TrackPoint fallback budget is included.
- [ ] BOM matches `docs/requirements.md` and `docs/architecture.md`.
