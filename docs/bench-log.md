# Phase 1 bench log

- **Status:** Phase 1 — template, measurements pending
- **Last updated:** 2026-11-05
- **Related:** [Bring-up](bringup.md), [Pin map](pinmap.md), [TrackPoint](trackpoint.md), [BOM](bom.md)

Record **measured values**, not just pass/fail. Every row needs a date, instrument, and evidence (photo, capture, or serial log). Do not mark a criterion passed without a measurement or observation.

## 0. Session setup

| Item | Value |
|---|---|
| Date | TBD |
| Operator | TBD |
| Multimeter | TBD (model, DC V / µA ranges) |
| Logic analyzer | TBD (model, sigrok driver) |
| Power source | TBD (USB / protected LiPo / other) |
| Firmware revision | TBD (git commit) |
| Bench shield revision | TBD (git commit) |
| Notes | TBD |

### Session plan

| Session | Scope | Depends on |
|---|---|---|
| 1 | Clone inventory, matrix, OLED, BLE split, Studio | Owned parts only |
| 2 | TrackPoint continuity, protocol, reset, driver | Logic analyzer + FPC adapters |
| 3 | Battery, charging, battery ADC, deep sleep, autonomy | Protected 502030 cells |
| 4 | BLE range with battery and magnets, antenna keepout | N52 magnets |
| Gate | Freeze pin map, accept ADR 0013, Phase 2 go/no-go | Sessions 1–4 |

## 1. Controller inventory and clone characterization

| Board | Markings / photos | 3.3 V (USB) | 3.3 V (battery) | UF2 mount | Settings reset | Baseline flash | Result |
|---|---|---:|---:|---|---|---|---|
| A | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| B | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| C | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| D | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

### 1.1 Electrical checks

| Check | Expected | Measured | Result | Notes |
|---|---|---|---|---|
| VCC–GND short (no power) | Open | TBD | TBD | |
| BAT–GND short (no battery) | Open | TBD | TBD | |
| 3.3 V rail, USB powered | 3.3 V ±5% | TBD | TBD | |
| USB input current, idle | Record | TBD | TBD | |
| Charger current, battery connected | Record | TBD | TBD | Do not charge unattended |
| Charge termination voltage | 4.20 V ±1% | TBD | TBD | Protected cell only |
| Battery ADC vs multimeter | Within tolerance | TBD | TBD | Internal VDDH or divider? |

### 1.2 Pin verification

Use the bench shield and a functional test for each pad. Record the method (matrix key, OLED, logic capture, or probe).

| Pad | Candidate function | Test method | Observed | Result |
|---|---|---|---|---|
| D0 | TrackPoint RX / CLK | TBD | TBD | TBD |
| D1 | TrackPoint TX / DATA | TBD | TBD | TBD |
| D2 | Display SDA / MOSI | TBD | TBD | TBD |
| D3 | Display SCL / SCK | TBD | TBD | TBD |
| D4 | Matrix row 0 | TBD | TBD | TBD |
| D5 | Matrix row 1 | TBD | TBD | TBD |
| D6 | Matrix row 2 | TBD | TBD | TBD |
| D7 | Matrix row 3 | TBD | TBD | TBD |
| D8 | Display CS / TrackPoint reset | TBD | TBD | TBD |
| D9 | TrackPoint reset / load switch | TBD | TBD | TBD |
| D14 | Matrix column | TBD | TBD | TBD |
| D15 | Matrix column | TBD | TBD | TBD |
| D18 | Matrix column | TBD | TBD | TBD |
| D19 | Matrix column | TBD | TBD | TBD |
| D20 | Matrix column | TBD | TBD | TBD |
| D21 | Matrix column | TBD | TBD | TBD |

## 2. Matrix

### 2.1 Left half

| Test | Expected | Observed | Result |
|---|---|---|---|
| Keys registering | 21/21 | TBD | TBD |
| Unused positions documented | 3 | TBD | TBD |
| Ghosting (3 keys, same row/column) | None | TBD | TBD |
| Stuck keys | None | TBD | TBD |
| Diode direction | col2row | TBD | TBD |

### 2.2 Right half

| Test | Expected | Observed | Result |
|---|---|---|---|
| Keys registering | 21/21 | TBD | TBD |
| Unused positions documented | 3 | TBD | TBD |
| Ghosting (3 keys, same row/column) | None | TBD | TBD |
| Stuck keys | None | TBD | TBD |
| Diode direction | col2row | TBD | TBD |

### 2.3 Split and host connectivity

| Test | Expected | Observed | Result |
|---|---|---|---|
| BLE split, both halves | Both halves type | TBD | TBD |
| BLE range, open room | ≥5 m | TBD | TBD |
| USB HID, host 1 | Works | TBD | TBD |
| USB HID, host 2 | Works | TBD | TBD |
| BLE HID, host 1 | Works | TBD | TBD |
| BLE HID, host 2 | Works | TBD | TBD |
| Three BLE profiles | Pair/switch | TBD | TBD |
| ZMK Studio over USB | Edit/persist | TBD | TBD |
| ZMK Studio over BLE | Edit/persist | TBD | TBD |

## 3. OLED

| Test | Expected | Observed | Result |
|---|---|---|---|
| I2C address | `0x3C` | TBD | TBD |
| Initializes | Status screen | TBD | TBD |
| Blank on idle | Blank | TBD | TBD |
| Wake behavior | 10 s ±2 s | TBD | TBD |
| Current, on | Record | TBD | TBD |
| Current, off/blank | Record | TBD | TBD |

## 4. TrackPoint

### 4.1 Identification and continuity

| Test | Expected | Observed | Result |
|---|---|---|---|
| Flex contact side | Top or bottom | TBD | TBD |
| Contact pitch | 0.5 mm | TBD | TBD |
| VCC/GND identification | Continuity/trace width | TBD | TBD |
| CLK/DATA identification | Continuity | TBD | TBD |
| Shorts between signals | None | TBD | TBD |

### 4.2 Power and logic

| Test | Expected | Observed | Result |
|---|---|---|---|
| Supply voltage | 3.3 V (do not assume 5 V) | TBD | TBD |
| Current, idle | Record | TBD | TBD |
| Current, active | Record | TBD | TBD |
| Power-up capture | CLK/DATA activity | TBD | TBD |
| PS/2 self-test | `0xAA` | TBD | TBD |
| Device ID | Record | TBD | TBD |
| Clock frequency | Record | TBD | TBD |

### 4.3 Reset and driver

| Test | Expected | Observed | Result |
|---|---|---|---|
| PS/2 reset `0xFF` | Repeatable init | TBD | TBD |
| RC reset | Repeatable init | TBD | TBD |
| MOSFET power-cycle | Repeatable init | TBD | TBD |
| GPIO driver fallback | Movement | TBD | TBD |
| Alternate baud | Movement | TBD | TBD |
| ZMK PS/2 driver | Movement | TBD | TBD |
| Clicks (left/right/middle) | Work | TBD | TBD |
| Scroll layer | Works | TBD | TBD |
| Reset repeated 5x | Works every time | TBD | TBD |

### 4.4 Firmware spike (offline)

| Test | Expected | Observed | Result |
|---|---|---|---|
| `kb_zmk_ps2_mouse_trackpoint_driver` PS/2 UART against ZMK v0.3.0 | Compiles | `CONFIG_PS2_UART=y`, `CONFIG_ZMK_INPUT_MOUSE_PS2=y` | PASS |
| Module custom `zmk,input-listener-ps2` | Compiles | Fails on removed `zmk/mouse/types.h` | FAIL |
| Native `zmk,input-listener` with `zmk,input-mouse-ps2` | Compiles | Build succeeds | PASS |
| Pin candidates D1/D0/D9 | Match driver recommendation | D1 SCL, D0 SDA, D9 RST | PASS (docs, hardware pending) |
| Hardware protocol/reset | Movement and repeatable init | TBD | TBD |

Pin the module revision `f6f3b30677caeccc4970bb48f48240d3504d03f7` when integrating. See [TrackPoint §5.1](trackpoint.md#51-zmk-v030-compatibility-spike-offline).

## 5. Power and autonomy

| Test | Expected | Observed | Result |
|---|---|---|---|
| 3.3 V rail, idle | 3.3 V ±5% | TBD | TBD |
| 3.3 V rail, OLED + TrackPoint active | 3.3 V ±5% | TBD | TBD |
| Ripple, idle | ≤100 mVpp | TBD | TBD |
| Ripple, active | ≤100 mVpp | TBD | TBD |
| Active current, OLED off | Record | TBD | TBD |
| Active current, OLED on | Record | TBD | TBD |
| TrackPoint idle current | Record | TBD | TBD |
| TrackPoint active current | Record | TBD | TBD |
| Deep-sleep current | Record | TBD | TBD |
| Implied average current | ≤0.75 mA for 2 weeks | TBD | TBD |
| Battery charge/termination | Correct | TBD | TBD |
| Battery level accuracy | ±10% | TBD | TBD |

**Instrument limitation:** there is no oscilloscope or bench supply on hand at the start of Phase 1. Record the method used for ripple and current; do not claim the ripple criterion without a valid measurement.

## 6. RF and mechanical notes

| Test | Expected | Observed | Result |
|---|---|---|---|
| BLE range, bare board | ≥5 m | TBD | TBD |
| BLE range, battery + magnets | ≥5 m; within 10% of bare | TBD | TBD |
| Antenna keepout | No battery/magnet over antenna | TBD | TBD |
| TrackPoint cap height | Document | TBD | TBD |
| Flex strain relief | Document | TBD | TBD |

## 7. Phase 1 exit checklist

- [ ] All 21 populated matrix positions per half register on the breadboard (42 total).
- [ ] OLED initializes and blanks correctly.
- [ ] TrackPoint responds to movement and clicks, or the fallback module is ordered.
- [ ] BLE split works between two nice!nano boards at ≥5 m.
- [ ] 3.3 V rail is within 3.3 V ±5% and ≤100 mVpp.
- [ ] Battery current, TrackPoint idle/active current, and deep-sleep current are measured and consistent with the autonomy target.
- [ ] The final pin map and TrackPoint wiring are agreed.
- [ ] ADR 0013 is accepted.
- [ ] Phase 2 go/no-go recorded in [Roadmap](roadmap.md).

## 8. Evidence index

| Evidence | Path / link | Notes |
|---|---|---|
| Controller photos | TBD | |
| Breadboard photos | TBD | |
| Logic captures | TBD | `.sr` files are generated artifacts; do not commit unless small and useful |
| Serial logs | TBD | |
| Measurement notes | TBD | |
