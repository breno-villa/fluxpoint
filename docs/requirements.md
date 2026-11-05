# Requirements

- **Status:** Phase 0 baseline, agreed at product level
- **Last updated:** 2026-11-05
- **Related:** [Architecture](architecture.md), [Roadmap](roadmap.md), [ADRs](decisions/README.md)

## 1. Objective and scope

### 1.1 Objective

Build a low-profile split keyboard that is comfortable on a desk, usable on a laptop or phone, and mountable to a chair arm or other surface with a magnetic interface. The keyboard must integrate a TrackPoint, a small status display, wireless split communication, USB operation, and a rechargeable battery per half. A future revision should support a fingerprint reader and a FIDO2/CTAP2 security key without compromising the keyboard.

### 1.2 Primary use cases

- Desk use with both halves flat or slightly tented.
- Laptop and smartphone/tablet use over BLE.
- Chair-arm or clamp-mounted use with adjustable angle.
- Travel with the keyboard only; mounts stay at home.
- Future security-key use with a fingerprint reader.

### 1.3 In scope for v1

- Corne 3x6+3 layout, 42 keys, Kailh Choc V1 hot-swap.
- Two mirrored PCBs, one controller per half.
- BLE split between halves and BLE/USB to the host.
- Salvaged Dell TrackPoint in the right thumb cluster.
- 0.91" 128x32 SSD1306 OLED on the right half, off by default, 10-second wake.
- 502030 250 mAh LiPo per half, USB-C charging, slide switch.
- 3D-printed case, FR4 switch plate, MBK blank keycaps.
- 4x N52 magnets, steel plate, 1/4"-20 ball head mount.
- ZMK firmware with ZMK Studio support.
- English documentation, public repository, CI, and project skills.

### 1.4 Out of scope for v1

- USB dongle.
- Fingerprint reader and FIDO2/CTAP2 implementation.
- Wired split between halves.
- RGB lighting.
- Wireless charging.
- Injection-molded or CNC case.
- Nice!view display purchase (footprint only).

## 2. Functional requirements

### 2.1 Keyboard and matrix

| ID | Requirement |
|---|---|
| FR-KB-01 | The keyboard **must** have 42 keys: 3 rows x 6 columns plus 3 thumb keys on each half (21 per half). |
| FR-KB-02 | Each half **must** use Kailh Choc V1 switches and hot-swap sockets. |
| FR-KB-03 | The matrix **must** use 1N4148W SOD-123 diodes and a col2row arrangement. |
| FR-KB-04 | The base keymap **must** be QWERTY with lower, raise, and adjust layers. |
| FR-KB-05 | The keymap **must** be editable at runtime through ZMK Studio without reflashing. |
| FR-KB-06 | The right thumb cluster **must** provide mouse left, right, and middle clicks for the TrackPoint, either as dedicated keys or on a pointing layer. |
| FR-KB-07 | A thumb key **must** enable a scroll layer while held; the final keymap defines which key. |

### 2.2 Connectivity

| ID | Requirement |
|---|---|
| FR-CON-01 | The halves **must** communicate over BLE split. |
| FR-CON-02 | The **right half** **must** be the central and support USB HID to a host; the TrackPoint is connected there, and v1 does not rely on ZMK input-split forwarding from a peripheral. |
| FR-CON-03 | The right half **must** support BLE HID to a host, including at least three paired hosts. |
| FR-CON-04 | The keyboard **must not** require a cable between halves during normal use. |
| FR-CON-05 | The firmware **must** be structured so a future dongle can become the central without changing the v1 hardware; the TrackPoint role in that configuration is a Phase 5 decision. |
| FR-CON-06 | Wired split, if added later, **must** use a separate protected UART link and must not backfeed VBUS. |
| FR-CON-07 | The left half's USB-C port **must** remain usable for charging and flashing, even though it is the peripheral. |

### 2.3 TrackPoint

| ID | Requirement |
|---|---|
| FR-TP-01 | The TrackPoint **must** be the salvaged Dell module with a black cap. |
| FR-TP-02 | The module **must** connect through its 4-pin, 0.5 mm FPC tail. |
| FR-TP-03 | The module **must** be mounted in the right thumb cluster and operated by the right thumb. |
| FR-TP-04 | Mouse buttons **must** be keyboard keys in the right thumb cluster, not dedicated switches. |
| FR-TP-05 | The firmware **must** provide sensitivity, axis, and scroll configuration. |
| FR-TP-06 | The design **must** include a reset strategy: PS/2 `0xFF`, RC reset, or controlled VCC power-cycle. |
| FR-TP-07 | If the salvaged module cannot be made to work, a known PS/2 TrackPoint module **must** be a documented electrical and mechanical fallback; the breakout and bracket must be adaptable. |

### 2.4 Display

| ID | Requirement |
|---|---|
| FR-DSP-01 | The v1 display **must** be a 0.91" 128x32 SSD1306 OLED over I2C, on the right half. |
| FR-DSP-02 | The OLED **must** be off by default. |
| FR-DSP-03 | A key combination **must** wake the OLED for 10 seconds, after which it turns off automatically. |
| FR-DSP-04 | The display **should** show battery, connection/output, and active layer; security status is shown only when a future security feature exists. |
| FR-DSP-05 | The final PCB **must** include a footprint or adapter path for a nice!view memory LCD. |

### 2.5 Power

| ID | Requirement |
|---|---|
| FR-PWR-01 | Each half **must** have its own protected 502030 250 mAh LiPo cell. |
| FR-PWR-02 | Each half **must** charge over its own USB-C port. |
| FR-PWR-03 | Each half **must** have a physical on/off switch. |
| FR-PWR-04 | The firmware **must** report battery level and enter deep sleep when idle. |
| FR-PWR-05 | The 3.3 V rail **must** supply the controller, OLED, and TrackPoint; the rail is measured in Phase 1 at 3.3 V ±5% with ≤100 mVpp ripple under the expected load. |
| FR-PWR-06 | The right PCB **must** include an unpopulated 4-pin UART header and load switch for a future fingerprint module. |
| FR-PWR-07 | The battery and magnets **must not** degrade BLE range below the acceptance target. |

### 2.6 Mechanical and magnetic mounting

| ID | Requirement |
|---|---|
| FR-MECH-01 | The case **must** be 3D-printable and use an FR4 switch plate. |
| FR-MECH-02 | The total height with MBK keycaps **must** be at most 16 mm. |
| FR-MECH-03 | Each half **must** weigh at most 250 g with battery. |
| FR-MECH-04 | The bottom **must** have 4x N52 magnet pockets and a flat seating area for desk use. |
| FR-MECH-05 | The magnetic interface **must** hold at least 2x the half's weight. |
| FR-MECH-06 | The mount **must** use a steel plate with a 1/4"-20 thread and a camera-style ball head. |
| FR-MECH-07 | The case **must** provide access to USB-C, reset, power switch, OLED, TrackPoint cap, and battery connector. |
| FR-MECH-08 | The TrackPoint bracket **must** support the module by its two ears and leave the bottom sensor grid clear. |
| FR-MECH-09 | The case **must** provide strain relief for the TrackPoint flex. |

### 2.7 Firmware and configuration

| ID | Requirement |
|---|---|
| FR-FW-01 | The firmware **must** be ZMK/Zephyr with custom modules where needed. |
| FR-FW-02 | The firmware **must** enable ZMK Studio and a Studio unlock binding. |
| FR-FW-03 | The final firmware **must** include the TrackPoint PS/2 driver and display behavior. |
| FR-FW-04 | The build **must** be reproducible through GitHub Actions and a local Docker command. |
| FR-FW-05 | A Flutter configurator **must** be delivered in Phase 4 for Android, Linux, Windows, and macOS. |
| FR-FW-06 | The configurator **must** support keymap/layers, keycodes/behaviors, and import/export. |
| FR-FW-07 | The configurator **should** support combos, macros, tap dances, TrackPoint/display/power settings, BLE profiles, DFU, and diagnostics. |
| FR-FW-08 | The v1 keyboard **must** remain fully usable without the Flutter configurator; ZMK Studio is the interim editor. |
| FR-FW-09 | The final shield **must** provide a ZMK Studio physical layout for the Fluxpoint keymap. |

### 2.8 Future security

| ID | Requirement |
|---|---|
| FR-SEC-01 | v1 **must not** implement FIDO2 or fingerprint authentication. |
| FR-SEC-02 | The right PCB **must** expose the future fingerprint header and load switch. |
| FR-SEC-03 | A future FIDO2 design **must** use a separate security architecture, not the ZMK keyboard firmware alone. |
| FR-SEC-04 | A future fingerprint implementation **must** define user-presence vs user-verification behavior and a fallback. |

## 3. Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-01 | Height ≤ 16 mm with keycaps. |
| NFR-02 | Weight ≤ 250 g per half with battery. |
| NFR-03 | Battery life ≥ 2 weeks under typical desktop use with the OLED off and the TrackPoint under its documented power policy (powered-idle or load-switched off); the policy and the implied average current of ≈0.75 mA must be validated in Phase 1. |
| NFR-04 | BLE end-to-end latency < 15 ms under normal typing. |
| NFR-05 | BLE range ≥ 5 m in an open room. |
| NFR-06 | Magnetic hold ≥ 2x the weight of one half. |
| NFR-07 | All 42 keys register reliably with no ghosting. |
| NFR-08 | TrackPoint must not drift when idle and must recover after power cycle. |
| NFR-09 | The keyboard must reconnect predictably after sleep or host switching. |
| NFR-10 | The case and PCB must be serviceable: socketed MCU, JST battery, hot-swap switches. |
| NFR-11 | The design must preserve Corne attribution and comply with MIT, CC BY 4.0, CERN-OHL-S-2.0, and documentation licensing. |
| NFR-12 | The repository must pass documentation, configuration, and baseline firmware checks in CI. |
| NFR-13 | The TrackPoint must not prevent the battery-life target; its idle and active current are measured in Phase 1 and a load switch or power policy is required if it exceeds the budget. |

## 4. Constraints

- Controller: Tenstar/SuperMini nice!nano v2 clone, nRF52840, socketed.
- Layout: Corne 3x6+3, 42 keys, Choc V1 spacing.
- Budget: R$ 500–1,500 target beyond parts already owned; the current BOM total upper estimate exceeds this, so tools/optional items must be trimmed before ordering.
- Timeline: no fixed deadline; milestone-based.
- Fabrication: 3D-printed case (printer borrowed), JLCPCB for PCBs, hand assembly.
- Bench: soldering station, multimeter, breadboard, ST-Link V2 (not used for nRF52 flashing), 8-channel logic analyzer to be purchased.
- Documentation and code in English.
- No FIDO2/fingerprint in v1.

## 5. Acceptance criteria

### 5.1 Keyboard

- [ ] All 42 keys register in a key tester, with no ghosting or stuck keys.
- [ ] Hot-swap sockets accept and retain Choc V1 switches.
- [ ] The QWERTY base layer, lower, raise, and adjust layers match the documented layout.
- [ ] ZMK Studio can unlock, edit, and persist a keymap over USB and BLE without reflashing.

### 5.2 TrackPoint

- [ ] The module responds to PS/2 self-test/identification (or the documented fallback is used).
- [ ] Movement is smooth at the default sensitivity; no drift when idle.
- [ ] Left, right, and middle clicks work from thumb keys.
- [ ] Scroll works while the scroll thumb key is held.
- [ ] A power cycle or reset sequence recovers the module reliably.

### 5.3 Display and power

- [ ] OLED is off by default and wakes for 10 s ± 2 s from the documented key combination.
- [ ] Battery level is reported within ±10% of a multimeter measurement.
- [ ] Each half charges from USB-C and stops at the correct voltage.
- [ ] 3.3 V rail is within 3.3 V ±5% and ≤100 mVpp with the display and TrackPoint active.
- [ ] Deep sleep current and TrackPoint idle/active current are measured; the documented TrackPoint power policy is consistent with ≥2 weeks of target use.

### 5.4 Connectivity

- [ ] BLE split works at ≥5 m with no dropouts during a 10-minute typing test.
- [ ] BLE latency is <15 ms in the test setup.
- [ ] USB HID works on Windows, Linux, and macOS.
- [ ] At least three BLE host profiles can be paired and switched.

### 5.5 Mechanical

- [ ] Assembled height is ≤16 mm at the keycaps.
- [ ] Each half weighs ≤250 g with battery.
- [ ] The magnetic interface holds ≥2x the half's weight and does not rotate during typing.
- [ ] The keyboard sits flat on a desk without wobble.
- [ ] The TrackPoint cap, OLED, USB-C, reset, and power switch are accessible.
- [ ] The case survives normal travel handling.

### 5.6 RF and safety

- [ ] BLE range with battery and magnets installed is within 10% of the bare-PCB range.
- [ ] No LiPo cell is charged without protection.
- [ ] No VBUS backfeed path exists between halves or accessories.
- [ ] The TrackPoint flex and battery wiring are strain-relieved.

### 5.7 Repository

- [ ] `python tools/fluxpoint_cli.py check-docs` passes.
- [ ] `python tools/fluxpoint_cli.py check-config` passes.
- [ ] `python -m pytest -q tools/tests` passes.
- [ ] The baseline firmware workflow builds left, right, and settings-reset UF2 files.
- [ ] BOM and bring-up documentation are complete enough to order parts and run Phase 1.

## 6. Open questions and risks

| Risk | Impact | Mitigation |
|---|---|---|
| TrackPoint protocol/reset unknown | Pointing device may not work | Breadboard test; logic analyzer; `0xFF`, RC, MOSFET; known-module fallback |
| TrackPoint FPC contact side unknown | Breakout may not mate | Breakout with top- and bottom-contact footprints |
| TrackPoint idle current | Battery-life target may be missed | Measure in Phase 1; add load switch/power policy; relax NFR-03 only with a recorded decision |
| Right-thumb bindings | Base keys, mouse clicks, and scroll compete for three keys | Define a pointing layer and final thumb keymap before the custom shield |
| Battery under MCU may detune antenna | Reduced BLE range | Antenna keepout, battery offset, range test |
| Magnetic mount vs flat desk | Wobble or weak hold | Magnet plane, feet, steel-plate recess, pull-force test |
| ZMK Studio limitations | Some settings need custom RPC | Phase 4 app features; document limitations |
| TrackPoint driver needs ZMK fork | Build complexity | Pin a tested fork/module revision in `west.yml`; test input-split behavior before relying on it |
| Fingerprint/FIDO2 architecture | Research risk | Keep v1 out of scope; expansion header only |
| 3D-printer tolerances | Case fit/height | Print test coupons; iterate |
| Procurement/import delays | Schedule slip | Order long-lead parts early; local alternatives |
| BOM cost overrun | Upper estimate exceeds R$ 1,500 before shipping | Trim tools/optional items; borrow the logic analyzer; combine PCB/plate panels |
| Exact pin budget | PCB rework | Close pin map before schematic; reserve spare GPIO |

## 7. References

- [Corne keyboard](https://github.com/foostan/crkbd)
- [nice!nano documentation](https://nicekeyboards.com/docs/nice-nano/)
- [ZMK split keyboards](https://zmk.dev/docs/features/split-keyboards)
- [ZMK Studio](https://zmk.dev/docs/features/studio)
- [ZMK pointing devices](https://zmk.dev/docs/features/pointing)
- [TrackPoint driver module](https://github.com/infused-kim/kb_zmk_ps2_mouse_trackpoint_driver)
- [nice!view](https://nicekeyboards.com/nice-view)
- [Kailh Choc V1](https://www.kailhswitch.com/)
- [HLK-ZW0905](https://www.hlktech.net/)
