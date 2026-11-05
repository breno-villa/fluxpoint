# Pin map

- **Status:** Phase 1 draft — **not frozen**
- **Last updated:** 2026-11-05
- **Related:** [Architecture](architecture.md), [Requirements](requirements.md), [Bring-up](bringup.md), [ADR 0013](decisions/0013-pin-map.md)

This document records the working pin map for the Phase 1 bench shield. The map is a candidate derived from the stock Corne shield and the documented nice!nano v2 board definition. It becomes the Phase 2 schematic input only after every function is verified on the clone at the pin-map gate.

## 1. Source and confidence

| Source | Use | Confidence |
|---|---|---|
| ZMK nice!nano v2 board DTS | Pro Micro pad to nRF52840 GPIO mapping | Documented; clone not yet measured |
| ZMK Corne shield | Candidate matrix rows/columns and I2C display pins | Known-good on a genuine nice!nano; clone pending |
| `docs/trackpoint.md` | TrackPoint signal functions and reset options | Protocol still unconfirmed |
| `docs/architecture.md` §5 | Pin budget and future expansion | Feasibility estimate |

The Tenstar/SuperMini clone may not expose the same set of pads or may route the charger/battery ADC differently. **Do not freeze a pin or start the Phase 2 schematic until the functional checks in §6 pass.**

## 2. Candidate map

`Pad` is the Pro Micro header name. `nRF` is the documented nice!nano v2 mapping; it is not a direct measurement of the clone.

| Pad | nRF52840 | Candidate function | Status | Notes |
|---|---|---|---|---|
| D0 | P0.08 | TrackPoint UART RX / CLK | Candidate | UART0 default RX; high-frequency capable |
| D1 | P0.06 | TrackPoint UART TX / DATA | Candidate | UART0 default TX; high-frequency capable |
| D2 | P0.17 | Display SDA / SPI MOSI | Candidate | nice!nano I2C SDA |
| D3 | P0.20 | Display SCL / SPI SCK | Candidate | nice!nano I2C SCL |
| D4 | P0.22 | Matrix row 0 | Candidate | Stock Corne row |
| D5 | P0.24 | Matrix row 1 | Candidate | Stock Corne row |
| D6 | P1.00 | Matrix row 2 | Candidate | Stock Corne row |
| D7 | P0.11 | Matrix row 3 | Candidate | Stock Corne row |
| D8 | P1.04 | Display CS / TrackPoint reset / load switch | Candidate | Shared function; resolve at the gate |
| D9 | P1.06 | TrackPoint reset / load switch | Candidate | Alternate to D8 |
| D10 | P0.09 | Spare / NFC | Avoid | NFC pin; needs `CONFIG_NFCT_PINS_AS_GPIOS` |
| D16 | P0.10 | Spare / NFC | Avoid | NFC pin; needs `CONFIG_NFCT_PINS_AS_GPIOS` |
| D14 | P1.11 | Matrix column (left 5 / right 6) | Candidate | Stock Corne column |
| D15 | P1.13 | Matrix column (left 4 / right 7) | Candidate | Stock Corne column |
| D18 | P1.15 | Matrix column (left 3 / right 8) | Candidate | Stock Corne column |
| D19 | P0.02 | Matrix column (left 2 / right 9) | Candidate | Stock Corne column |
| D20 | P0.29 | Matrix column (left 1 / right 10) | Candidate | Stock Corne column |
| D21 | P0.31 | Matrix column (left 0 / right 11) | Candidate | Stock Corne column |

### Matrix detail

- 4 rows x 6 columns per half, 21 populated positions per half.
- `diode-direction = "col2row"`.
- Left columns, in order: D21, D20, D19, D18, D15, D14.
- Right columns, in order: D14, D15, D18, D19, D20, D21.
- The right half uses `col-offset = <6>` in the matrix transform.
- The three unused positions are documented in the bench log after the breadboard is wired.

### Battery ADC

The nice!nano v2 board definition uses the internal VDDH measurement (`zmk,battery-nrf-vddh`), so no header pin is reserved. The clone may use an external divider; verify the battery reading against a multimeter in Phase 1. If a divider pin is required, D8/D9 are the first candidates, but they conflict with the display CS / TrackPoint reset / load-switch functions.

### Future expansion

| Function | Pins | v1 | Notes |
|---|---:|---|---|
| Fingerprint UART | 2 | No | Header unpopulated; reserved in Phase 2 |
| Fingerprint load switch | 1 | No | Header unpopulated |
| TrackPoint reset / load switch | 1 | Optional | D8 or D9 candidate |
| Display CS (nice!view) | 1 | No | Shared 3-GPIO header; OLED uses D2/D3 only |
| Spare / test points | 1–2 | — | Keep for bring-up |

## 3. Pin budget

| Function | Pins | v1 populated | Future |
|---|---:|---|---|
| Matrix rows | 4 | Yes | — |
| Matrix columns | 6 | Yes | — |
| TrackPoint CLK/DATA | 2 | Yes | — |
| TrackPoint reset/load switch | 1 | Optional | — |
| Display header (I2C OLED or SPI nice!view) | 3 | Yes | Shared; OLED uses 2, nice!view uses 3 |
| Battery ADC | 0–1 | Yes | Internal VDDH; reserve 1 if the clone uses a divider |
| Fingerprint UART | 2 | No | Header, unpopulated |
| Fingerprint load switch | 1 | No | Header, unpopulated |
| Spare/test points | 1–2 | — | Bring-up |

The Pro Micro header exposes **18 GPIO** on the documented nice!nano v2. The v1 populated budget is 16–17 pins. Adding the future fingerprint header brings it to 19–20, which exceeds 18 unless:

- the clone exposes additional GPIO pads (the “21 GPIO” figure must be verified);
- the NFC pins P0.09/P0.10 are enabled as GPIO;
- the display CS and fingerprint load switch share a pin (they are not active at the same time);
- an I2C GPIO expander is added; or
- the fingerprint header is reduced or moved to a later board revision.

This is a Phase 1 gate item, not a Phase 2 surprise.

## 4. Constraints

- Do not use the NFC pins P0.09/P0.10 without explicitly enabling them as GPIO.
- Avoid the SWD, USB, reset, LED, charger, and `EXT_POWER` pins.
- Prefer high-frequency-capable pins for the TrackPoint UART to reduce BLE interference.
- The shared display header must support both I2C (OLED) and 3-wire SPI (nice!view) on the same three pads. Confirm the chosen pins can be remapped by pinctrl for both peripherals.
- I2C needs pull-ups; confirm whether they are on the display module or the PCB.
- The battery ADC must be measured against a multimeter before trusting the percentage.
- Any change after the pin-map gate requires a new ADR or a superseding update to ADR 0013.

## 5. Phase 1 bench shield

The temporary shield lives in `firmware/zmk-config/config/boards/shields/fluxpoint_bench/`:

- `fluxpoint_bench_left` — peripheral, matrix only.
- `fluxpoint_bench_right` — central, matrix + I2C OLED.

The shield uses the candidate map above and is built in CI. It is a test artifact, not the final shield.

## 6. Pin-map gate checklist

- [ ] Clone Pro Micro pad labels and physical order match the documented nice!nano v2.
- [ ] All 4 rows and 6 columns scan correctly on both halves.
- [ ] OLED initializes at `0x3C` on D2/D3.
- [ ] TrackPoint CLK/DATA work on the chosen UART pins; capture shows valid PS/2.
- [ ] Reset/load-switch pin (if used) toggles correctly.
- [ ] Battery ADC reading matches a multimeter within the expected tolerance.
- [ ] Shared display header supports I2C and SPI without pin conflicts.
- [ ] Future fingerprint pins are either reserved or the limitation is documented.
- [ ] No conflict with SWD, USB, reset, LED, charger, or NFC.
- [ ] ADR 0013 is accepted and the final map is copied to the Phase 2 schematic notes.
