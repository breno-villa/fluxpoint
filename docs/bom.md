# BOM and inventory

- **Status:** Phase 1 estimate; the Phase 1 batch in §8 is pending approval
- **Last updated:** 2026-11-05
- **Currency:** BRL (R$), approximate; adjust for your region and import taxes
- **Related:** [Requirements](requirements.md), [Roadmap](roadmap.md), [TrackPoint](trackpoint.md)

## 1. Owned inventory

| Item | Qty | Notes |
|---|---:|---|
| Tenstar/SuperMini nice!nano v2 clone (nRF52840) | 4 | Two halves, one dongle/spare later |
| Kailh Choc V1 switches | 100 | Low-profile, 5-pin |
| Kailh Choc hot-swap sockets | 100 | For Choc V1 |
| 1N4148 through-hole diodes | 100 | Breadboard/prototype use |
| 1N4148W SOD-123 diodes | 100 | Final PCB matrix |
| MSK-12C02 on/off switches (1P2T SPDT SMD) | 2+ | Quantity to confirm; one per half |
| TRRS PJ-320A connector | 1+ | Owned but not used in v1 |
| HLK-ZW0905 fingerprint sensor | 1 | Owned, deferred to Phase 5 |
| SSD1306 0.91" 128x32 I2C OLED | 1 | v1 display |
| Dell TrackPoint module with black cap | 1 | Salvaged from Latitude 0D19TR keyboard |
| Breadboard | 1 | Phase 1 |
| Soldering station, multimeter, basic tools | 1 set | Phase 1 |
| ST-Link V2 | 1 | Not used for nRF52 UF2 flashing; may help with other MCUs |
| 3D printer | borrowed | Prototype case/plates |

## 2. Missing parts for v1

| Item | Qty | Estimate (R$) | Supplier | Notes |
|---|---:|---:|---|---|
| MBK blank Choc keycaps | 42 | 150–300 | AliExpress | Choc V1, blank; color TBD |
| 502030 250 mAh LiPo with PCM and JST-PH | 2 | 60–100 | AliExpress | Protected cell; verify polarity |
| Left PCB | 1 | 80–150 | JLCPCB | 2-layer, 1.6 mm, HASL |
| Right PCB | 1 | 80–150 | JLCPCB | Mirrored; same panel as left if possible |
| FR4 switch plate | 2 | 50–100 | JLCPCB | 1.2–1.6 mm |
| N52 neodymium magnets, 8x2 or 10x2 mm | 8 | 40–80 | AliExpress | 4 per half; size finalized after pull test |
| Steel plate 1 mm with 1/4"-20 boss | 2 | 60–120 | Local/online | Magnetic target for each half |
| Camera ball head + clamp | 2 | 100–200 | Local/online | Desk/chair-arm mount; 1/4"-20 |
| Screws, standoffs, inserts | 1 set | 30–60 | Local | M1.4/M2; case/PCB/plate |
| JST-PH connectors and wires | 1 set | 20–40 | Local/AliExpress | Battery and power |
| USB-C data/charging cables | 2 | 20–40 | Local | One per half; data-capable for flashing |
| Heat-shrink, tape, rubber feet | 1 set | 20–40 | Local | Strain relief and desk feet |
| 4-pin FPC 0.5 mm top contact | 2 | 10–20 | AliExpress | TrackPoint breakout/main PCB |
| 4-pin FPC 0.5 mm bottom contact | 2 | 10–20 | AliExpress | Alternative contact side |
| 4-pin FPC 0.5 mm breakout adapter, top contact | 2 | 10–20 | AliExpress | Bench adapter; mates the flex without a custom PCB |
| 4-pin FPC 0.5 mm breakout adapter, bottom contact | 2 | 10–20 | AliExpress | Alternative contact side |
| 4-pin 2.54 mm header / JST-SH | 2 | 5–10 | Local | Breakout/PCB |
| 4.7 kΩ, 100 kΩ resistors; 2.2 µF cap | 1 set | 5–10 | Local | PS/2 pull-ups and RC reset |
| P-MOSFET/load switch for TrackPoint/fingerprint | 2 | 10–20 | Local | Optional reset/power control |
| 8-channel 24 MHz USB logic analyzer | 1 | 50–100 | AliExpress | TrackPoint protocol bring-up |
| PETG/ABS filament | 1 spool | 50–100 | Local | Case/plate prototypes |
| TrackPoint breakout PCB | 5 | 20–40 | JLCPCB | Small board; can share panel |
| Schottky diode SS14/BAT54 (optional) | 10 | 10–20 | Local | Backfeed/protection experiments |
| Known PS/2 TrackPoint module (fallback) | 1 | 50–150 | AliExpress/local | Contingency only; not included in the base total |
| Nice!view display | 0 | 0 | — | Not purchased in v1; final PCB footprint only |
| Fingerprint wiring/header | 0 | 0 | — | Header/load switch unpopulated in v1 |

**Estimated totals:**

- **Keyboard parts:** R$ 770–1,500, including the prototype TrackPoint breakout PCB and USB-C cables, excluding tools/consumables and the optional Schottky diodes.
- **Tools and consumables:** R$ 100–200 for the logic analyzer and filament; the logic analyzer is listed in §3, and the filament is a case consumable.
- **Total for the v1 build:** R$ 870–1,700 before shipping/import taxes.
- **Contingency:** R$ 50–150 for a known PS/2 TrackPoint module if the salvaged Dell module cannot be used; R$ 10–20 for the optional Schottky experiments.

The R$ 1,500 budget target is reachable for the keyboard parts at the upper estimate, but the total exceeds it once tools and shipping are included. Trim by borrowing the logic analyzer, using local filament, combining PCB/plate panels, or deferring optional items. Quotes for PCBs and plates assume a small panel/order; the table lists the quantity needed for one keyboard, not the minimum order quantity.

## 3. Tools and test equipment

| Tool | Status | Use |
|---|---|---|
| Soldering station | Owned | Assembly and rework |
| Multimeter | Owned | Continuity, voltage, current |
| Breadboard + jumpers | Owned | Phase 1 |
| 8-channel logic analyzer | Buy | PS/2/UART decoding; included in the tools total in §2 |
| Bench power supply | Optional | Current-limited TrackPoint/fingerprint tests; borrow first |
| Oscilloscope | Optional | Ripple, signal integrity; borrow first |
| USB-C power meter | Optional | Charge current/voltage; useful but not required |
| Fine-tip probes / pogo pin set | Optional | Probing the flex/test points; not a substitute for the FPC connector |
| Calipers | Owned | Case/PCB measurements |
| 3D printer | Borrowed | Case/plate prototypes |
| UV/weathering setup | Optional | Case finish |

A bench supply or oscilloscope is not required for every Phase 1 test, but two measurements do need them: first TrackPoint power-up needs current limiting, and the ripple criterion needs a scope. Borrow them first; buy only if borrowing is not possible and the measurement is on the critical path.

## 4. PCB and assembly notes

- PCB: 2 layers, 1.6 mm, HASL, 1 oz copper; ENIG optional for fine-pitch pads.
- PCB and FR4 plate estimates assume a small panel/order (typically 5 boards); the table quantity is per keyboard, not the minimum order quantity. Combine left/right PCBs, plates, and the TrackPoint breakout in one order where possible.
- Switch plate: FR4 1.2–1.6 mm; 1.2 mm preferred for height, 1.6 mm for stiffness.
- Controller: socketed with 2.54 mm headers; do not solder the nice!nano directly.
- Hot-swap sockets: through-hole; verify orientation before soldering.
- Diodes: 1N4148W SOD-123; check polarity marking and orientation.
- TrackPoint: FPC connector 0.5 mm; breakout board with both top/bottom contact footprints; strain relief on the flex.
- Battery: JST-PH connector, protected cell; verify polarity with a multimeter before plugging in.
- Magnets: embed with glue; ensure polarity is consistent between halves and mounts.
- Case: print a fit coupon first; PETG or ABS; 0.2 mm layers; 3–4 perimeters.

## 5. TrackPoint breakout BOM

| Ref | Part | Qty | Notes |
|---|---|---:|---|
| J1 | FPC 4-pin 0.5 mm, top contact | 1 | Populate one of J1/J2 |
| J2 | FPC 4-pin 0.5 mm, bottom contact | 1 | Alternative contact side |
| J3 | 4-pin 2.54 mm header or JST-SH | 1 | VCC/GND/CLK/DATA |
| R1, R2 | 4.7 kΩ pull-ups | 2 | CLK/DATA to 3.3 V |
| R3, R4 | 4.7 kΩ | 2 | RC reset |
| R5 | 100 kΩ | 1 | RC reset |
| C1 | 2.2 µF | 1 | RC reset |
| C2 | 1–10 µF | 1 | Bulk decoupling |
| Q1 | P-MOSFET/load switch | 1 | Optional power-cycle |
| TP1–TP4 | Test points | 4 | Logic analyzer |

## 6. Supplier strategy

- **JLCPCB:** PCBs, FR4 plates, breakout PCB; combine designs in one order/panel when possible.
- **AliExpress:** keycaps, batteries, magnets, FPC connectors, logic analyzer; order long-lead items early.
- **Local/national:** screws, standoffs, wire, heatshrink, filament, ball heads/clamps, steel plates.
- **Fallback:** known PS/2 TrackPoint module if the salvaged Dell module cannot be used; budget R$ 50–150.

## 7. Open procurement questions

- Exact magnet size/pull force after test.
- Steel plate dimensions/thread boss supplier.
- Battery connector polarity and wire length.
- FPC contact side; buy both top and bottom connectors.
- Keycap color/legend preference; MBK blank is assumed.
- Whether to order 5 or 10 PCBs to allow rework; confirm minimum order quantities and panelization for PCBs and FR4 plates.
- Whether the logic analyzer can be borrowed or shared to keep the build within budget.
- Fallback TrackPoint module supplier, price, and mechanical fit.
- USB-C cable data rating; charge-only cables are not sufficient for flashing.
- Import taxes and lead times for JLCPCB/AliExpress.

## 8. Phase 1 procurement batch (pending approval)

This is the first order list for Phase 1. It is a subset of §2/§3, not an additional build. **Do not purchase until the list is approved.** Prices are estimates; confirm supplier, minimum order quantity, and shipping before ordering.

| Priority | Item | Qty | Estimate (R$) | Supplier | Purpose |
|---:|---|---:|---:|---|---|
| 1 | 8-channel 24 MHz logic analyzer | 1 | 50–100 | AliExpress | PS/2 capture and decode; confirm sigrok support |
| 1 | FPC 0.5 mm 4-pin breakout adapter, top contact | 2 | 10–20 | AliExpress | Immediate bench connection to the TrackPoint flex |
| 1 | FPC 0.5 mm 4-pin breakout adapter, bottom contact | 2 | 10–20 | AliExpress | Contact side is still unconfirmed |
| 1 | 502030 250 mAh protected LiPo with JST-PH | 2 | 60–100 | AliExpress | Charger, battery ADC, autonomy tests |
| 1 | USB-C data cable | 2 | 20–40 | Local | Flashing and charging; charge-only cables are not enough |
| 2 | 4-pin FPC 0.5 mm connector, top contact | 2 | 10–20 | AliExpress | Custom TrackPoint breakout PCB |
| 2 | 4-pin FPC 0.5 mm connector, bottom contact | 2 | 10–20 | AliExpress | Custom TrackPoint breakout PCB |
| 2 | N52 magnets, 8x2 or 10x2 mm | 8 | 40–80 | AliExpress | RF/keepout test; final size after pull test |
| 2 | Resistors 4.7 kΩ / 100 kΩ, caps 2.2 µF / 1–10 µF | 1 set | 5–10 | Local | Pull-ups, RC reset, decoupling |
| 2 | P-MOSFET / load switch | 2 | 10–20 | Local | TrackPoint power-cycle / power policy |
| 2 | 4-pin 2.54 mm header or JST-SH | 2 | 5–10 | Local | Breakout/PCB |
| 2 | TrackPoint breakout PCB fabrication | 5 | 20–40 | JLCPCB | Phase 1 deliverable; can share a panel |
| 3 | USB-C power meter | 1 | 20–50 | AliExpress | Charge current/voltage; optional |
| 3 | Fine-tip probes / pogo pin set | 1 | 20–50 | AliExpress | Probing the flex/test points; optional |
| Borrow | Bench power supply | 1 | 0–250 | Local/maker space | Current-limited first power-up; borrow first |
| Borrow | Oscilloscope | 1 | 0–300+ | Local/maker space | Ripple measurement; borrow first |

**Batch estimate:** R$ 250–480 for priorities 1–2, most of which is already in the §2 total. The adapter and probe items add about R$ 40–90 to the tools/bench estimate. Bench supply and oscilloscope are borrow-first.

**Minimum viable order if the budget is tight:** logic analyzer, one top-contact and one bottom-contact FPC breakout adapter, two protected cells, USB-C cables, and the passives. The custom breakout PCB and magnets can follow after the first bench session, but they are on the Phase 1 critical path.
