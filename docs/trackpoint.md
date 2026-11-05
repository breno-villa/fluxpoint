# TrackPoint integration

- **Status:** Phase 1 validation
- **Last updated:** 2026-11-05
- **Related:** [Architecture](architecture.md), [Bring-up](bringup.md), [BOM](bom.md), [ADR 0005](decisions/0005-trackpoint.md)

## 1. Module identification

The module was salvaged from a Dell Latitude 0D19TR keyboard (compatible with Latitude 5480/5490/E5450/E5470/E7450/E7470). It is the pointing-stick sensor, not the full keyboard assembly.

| Property | Measurement | Confidence |
|---|---|---|
| Sensor PCB | ~13.5 x 10.9 mm | Caliper |
| Thickness | ~3.9 mm | Caliper, zeroed |
| Mounting-hole spacing | ~12.8 mm | Caliper, approximate |
| Flex | 4 conductors | Visual |
| Connector | 4-pin FPC, 0.5 mm pitch | Caliper + connector body width |
| Cap | Black rubber dome, present | Visual |
| Bottom | Black sensor grid; keep clear | Visual |

The earlier unzeroed caliper readings (3.5 mm, 12.7 mm) are superseded by the zeroed measurements (3.9 mm, 12.8 mm). Use 3.9 mm and 12.8 mm as working values and re-measure before finalizing the case.

## 2. Electrical interface

The 4-wire flex is most likely PS/2:

| Signal | Likely function | Notes |
|---|---|---|
| VCC | 3.3 V | Confirm with continuity/trace width; do not assume 5 V |
| GND | Ground | Usually the widest trace |
| CLK | PS/2 clock | Needs pull-up to 3.3 V |
| DATA | PS/2 data | Needs pull-up to 3.3 V |

The module may also be I2C or analog. The protocol is confirmed in Phase 1 with a logic analyzer. Do not apply 5 V until the original keyboard's rail is confirmed; 3.3 V is the working assumption.

### Reset

Many TrackPoints require a power-on-reset sequence. This module has only four wires, so the reset may be internal, a PS/2 `0xFF` command may work, or a controlled VCC power-cycle may be required. The design reserves:

- an RC reset circuit (2x 4.7 kΩ, 100 kΩ, 2.2 µF);
- a P-MOSFET/load-switch option for power-cycling VCC;
- a GPIO reset option if the module exposes a reset behavior through one of the lines.

## 3. Connector and breakout

The flex terminates in a 4-pin, 0.5 mm pitch FPC connector. The contact side (top vs bottom) is still unconfirmed. The breakout board therefore provides two footprints:

- J1: 4-pin FPC, 0.5 mm, top contact;
- J2: 4-pin FPC, 0.5 mm, bottom contact.

Populate the one that mates with the flex. The breakout also includes:

- 4-pin 2.54 mm header or JST-SH for VCC/GND/CLK/DATA;
- 4.7 kΩ pull-ups on CLK/DATA;
- RC reset components;
- optional MOSFET power-cycle;
- test points for the logic analyzer;
- bulk decoupling (1–10 µF).

### Bench connection strategy

Use a 4-pin 0.5 mm FPC breakout adapter (top and bottom contact variants) as the primary bench connection. A pogo pin or fine probe is useful for **probing** the flex or test points, but it is not a reliable substitute for a ZIF connector at 0.5 mm pitch: alignment is difficult and a slip can short adjacent contacts. Probe at the 2.54 mm header or the breakout test points, not directly on the flex, once the adapter is mated.

## 4. Mechanical integration

- Position: right thumb cluster, below/next to the three thumb keys.
- Orientation: cap up, bottom sensor grid facing down with clearance.
- Mounting: use the two ears/holes (≈12.8 mm spacing) with M1.4/M1.6 screws or a 3D-printed bracket.
- Do not glue or press the bottom black grid; it is the sensor surface.
- The module is ~3.9 mm thick; the black cap adds height. The cap top must remain below or level with the keycaps and accessible to the thumb.
- Provide strain relief for the flex near the FPC connector; avoid sharp bends and pulling on the solder joint.
- The case must allow the FPC connector to be unplugged for service.

## 5. Firmware

- Use the ZMK PS/2 driver module (`kb_zmk_ps2_mouse_trackpoint_driver`) or an equivalent implementation.
- Prefer the UART-based PS/2 driver on nRF52; the GPIO driver is a fallback.
- Use high-frequency pins for the UART if possible to avoid BLE interference.
- Configure sensitivity, axis inversion, and scroll behavior.
- Mouse buttons are right thumb keys, either dedicated or on a pointing layer; scroll is a held thumb layer.
- Test press-to-select only if the module supports it; it is optional.

### 5.1 ZMK v0.3.0 compatibility spike (offline)

ZMK v0.3.0 has official pointing support (`CONFIG_ZMK_POINTING`, `zmk,input-listener`, and input processors). The `kb_zmk_ps2_mouse_trackpoint_driver` module's lower-level PS/2 UART driver and its `zmk,input-mouse-ps2` input driver compile against v0.3.0. Its custom `zmk,input-listener-ps2` does **not**: it includes the removed `zmk/mouse/types.h`.

Use the module's PS/2 input driver with ZMK's native `zmk,input-listener`, not the module's listener:

```dts
/ {
    mouse_ps2: mouse_ps2 {
        compatible = "zmk,input-mouse-ps2";
        ps2-device = <&uart_ps2>;
        rst-gpios = <&pro_micro 9 GPIO_ACTIVE_HIGH>;
        status = "okay";
    };

    mouse_ps2_listener: mouse_ps2_listener {
        compatible = "zmk,input-listener";
        device = <&mouse_ps2>;
        status = "okay";
    };
};
```

The PS/2 UART driver uses D1 (SCL), D0 (SDA), and D9 (RST); this matches the high-frequency pin recommendation and the pin-map candidate. Build the spike with `-DZMK_EXTRA_MODULES=<path-to-module>` and `-DCONFIG_ZMK_POINTING=y`. Pin the module revision `f6f3b30677caeccc4970bb48f48240d3504d03f7` when integrating it into `west.yml`.

This proves compilation only. The hardware protocol, reset sequence, and movement still need the Phase 1 bench session. Re-check the module before integration; its custom listener may be fixed upstream later.

## 6. Test plan

1. **Continuity:** identify VCC/GND by trace width and continuity; do not guess polarity.
2. **Power:** 3.3 V with a 100 mA limit; measure current.
3. **Logic capture:** CLK/DATA at power-up; decode PS/2; look for `0xAA`.
4. **Driver:** connect to a nice!nano; build the ZMK PS/2 configuration; test movement.
5. **Reset:** try `0xFF`; then RC; then MOSFET power-cycle; then GPIO driver/baud alternatives.
6. **Fallback:** if the module is I2C/analog or damaged, use a known PS/2 TrackPoint module.

## 7. Fallback

If the Dell module cannot be made to work, use a known PS/2 TrackPoint module with documented pinout and 3.3 V compatibility. The case bracket and breakout should be adaptable; the main PCB footprint can remain the same 4-pin FPC/header.

## 8. Open questions

- Exact contact side (top/bottom).
- Protocol (PS/2 vs I2C vs analog).
- Reset behavior.
- VCC rail and current.
- Cap height and final stack-up.
- Bracket screw size and hole tolerance.
- Flex length and routing inside the case.
