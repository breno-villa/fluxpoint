# Bring-up and acceptance tests

- **Status:** Phase 0 procedure
- **Last updated:** 2026-11-05
- **Related:** [Requirements](requirements.md), [TrackPoint](trackpoint.md), [BOM](bom.md), [Automation](automation.md)

## 1. Safety

- LiPo cells: use a protected cell, never charge unattended, verify polarity before connecting, and do not puncture or bend the pouch.
- Current-limit the bench supply to 100 mA for first power-up and 300 mA for TrackPoint/fingerprint tests.
- Disconnect power before changing wiring.
- Treat the TrackPoint flex as fragile: support the stiffener, avoid sharp bends, and never pull the flex to unplug it.
- Use ESD precautions around the controller and TrackPoint module.
- Do not hot-plug a wired split link; v1 has no wired split.

## 2. Phase 1 — bench characterization

### 2.1 nice!nano clone

1. Photograph both sides and record markings.
2. Check for shorts between VCC, GND, and battery pads with a multimeter.
3. Verify the 3.3 V output with USB connected.
4. Measure the charger behavior with a protected LiPo: charge current, termination voltage, and battery voltage reporting.
5. Confirm the UF2 bootloader mount name and flash a settings-reset UF2.
6. Record the exact pin mapping; compare it with the documented nice!nano v2 pinout.

**Pass:** boots, enumerates as UF2, 3.3 V stable, charger works, no overheating.

### 2.2 Matrix breadboard

1. Wire a 4x6 matrix with 1N4148 through-hole diodes, col2row.
2. Use the baseline ZMK Corne firmware with the same row/column pins, or build a temporary shield.
3. Test every key with a key tester.
4. Check for ghosting by pressing combinations of three keys in the same row/column.

**Pass:** all 24 positions register; no ghosting; no stuck keys.

### 2.3 OLED

1. Connect the SSD1306 to 3.3 V, GND, SDA, SCL.
2. Scan I2C; expect address `0x3C`.
3. Build the baseline firmware with `CONFIG_ZMK_DISPLAY=y`.
4. Verify the status screen and blank-on-idle behavior.

**Pass:** display initializes, shows status, blanks, and wakes.

### 2.4 TrackPoint

1. Inspect the flex and connector; confirm 4 contacts and 0.5 mm pitch.
2. Use the breakout with both top/bottom FPC footprints; populate the one that mates.
3. Identify VCC/GND by trace width/continuity; do not guess polarity.
4. Power at 3.3 V with a 100 mA limit; measure current.
5. Capture CLK/DATA with the logic analyzer at power-up.
6. Decode PS/2; look for the `0xAA` self-test response.
7. Connect to a nice!nano and build the ZMK PS/2 driver configuration.
8. If initialization fails, try:
   - PS/2 reset command `0xFF`;
   - RC reset circuit;
   - controlled VCC power-cycle via MOSFET;
   - GPIO driver instead of UART;
   - alternate UART baud rate.
9. If the module is I2C or analog, stop and document the finding; switch to the known-module fallback.

**Pass:** movement reports on the logic analyzer and in the host; clicks/scroll work; reset is repeatable.

### 2.5 Power and BLE

1. Measure active current with OLED on/off and TrackPoint idle/moving.
2. Measure deep-sleep current after the configured timeout.
3. Measure BLE range with the battery and magnets in the intended positions.
4. Test USB HID and BLE HID on at least two hosts.
5. Verify charging from USB-C and battery level reporting.

**Pass:** current is consistent with ≥2 weeks autonomy; range ≥5 m; charging terminates correctly.

## 3. Phase 2 — PCB and case bring-up

### 3.1 Visual and electrical

- Inspect for solder bridges, missing components, and diode orientation.
- Check 3.3 V and GND rails for shorts before inserting the controller.
- Insert the controller only after the rails are verified.
- Check the TrackPoint FPC connector orientation and latch.

### 3.2 Matrix and controller

- Flash the custom shield.
- Test every key; verify the matrix transform.
- Test the reset/bootloader access.
- Test the power switch and battery connection.

### 3.3 TrackPoint and display

- Verify TrackPoint movement, clicks, scroll, and reset.
- Verify OLED wake/blank timing (10 s ± 2 s).
- Verify the nice!view footprint/adaptor if populated.

### 3.4 Mechanical

- Assemble the case, plate, PCB, battery, magnets, and TrackPoint.
- Measure height at the keycaps and at the controller/battery area.
- Weigh each half.
- Test magnetic hold with the steel plate and ball head.
- Test flat desk seating and wobble.
- Test access to USB-C, reset, power switch, OLED, and TrackPoint cap.

### 3.5 RF

- Measure BLE range with and without the battery/magnets/case.
- Check for dropouts while typing and while the TrackPoint moves.
- If range degrades, adjust battery offset/antenna keepout or magnet placement.

## 4. Acceptance test checklist

Copy this checklist into the release notes and record measured values.

### Keyboard

- [ ] 42 keys register, no ghosting.
- [ ] Hot-swap sockets retain switches.
- [ ] QWERTY/lower/raise/adjust layers match [Layout](layout.md).
- [ ] ZMK Studio unlock/edit/persist over USB.
- [ ] ZMK Studio unlock/edit/persist over BLE.

### TrackPoint

- [ ] Movement smooth, no idle drift.
- [ ] Left/right/middle clicks from thumb keys.
- [ ] Scroll while holding the scroll thumb key.
- [ ] Reset/power-cycle recovery, repeated 5 times.

### Display and power

- [ ] OLED off by default.
- [ ] Wake combo turns display on for 10 s ± 2 s.
- [ ] Battery level within ±10%.
- [ ] USB-C charging works on both halves.
- [ ] Deep-sleep current recorded.

### Connectivity

- [ ] BLE split ≥5 m, 10-minute typing test.
- [ ] BLE latency <15 ms.
- [ ] USB HID on Windows/Linux/macOS.
- [ ] Three BLE host profiles paired/switched.

### Mechanical

- [ ] Height ≤16 mm at keycaps.
- [ ] Weight ≤250 g per half.
- [ ] Magnetic hold ≥2x half weight.
- [ ] No wobble on desk.
- [ ] Access to all connectors/switches.
- [ ] Travel handling test.

### RF/safety

- [ ] Range with battery/magnets within 10% of bare PCB.
- [ ] Protected LiPo only.
- [ ] No VBUS backfeed path.
- [ ] Flex/battery strain relief.

## 5. Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| Controller not detected | Bootloader/UF2 issue, cable, short | Try another cable; check 3.3 V; double-tap reset |
| Keys missing | Diode orientation, matrix pin map, solder joint | Continuity test; compare transform |
| Ghosting | Missing diodes, wrong diode direction | Check col2row and diode polarity |
| OLED blank | I2C address, wiring, display config | Scan I2C; check `CONFIG_ZMK_DISPLAY` |
| TrackPoint no movement | Pinout, reset, power, protocol | Logic analyzer; try `0xFF`, RC, MOSFET; check 3.3 V |
| TrackPoint drift | Calibration/sensor damage | Recalibrate; test another module |
| BLE range poor | Antenna keepout, battery/magnets, case | Move battery; test bare PCB; check case material |
| Battery not charging | Polarity, charger, cell protection | Verify polarity; measure charge current; try another cell |
| ZMK Studio cannot connect | USB/BLE output mismatch, permissions, firmware config | Match output endpoint; check udev/dialout; verify Studio build |
