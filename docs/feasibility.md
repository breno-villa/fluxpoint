# Feasibility assessment

- **Status:** Phase 0 baseline
- **Last updated:** 2026-11-05
- **Related:** [Requirements](requirements.md), [Architecture](architecture.md), [TrackPoint](trackpoint.md), [Roadmap](roadmap.md)

This document separates what is already proven from what still needs a prototype. It is a planning tool, not a guarantee.

## Summary

| Subsystem | Feasibility | Evidence | Main risk | Next step |
|---|---|---|---|---|
| 42-key Choc matrix | High | Standard Corne/Choc designs; parts on hand | Hot-swap and diode layout space | Breadboard matrix |
| nice!nano clone + ZMK | High | ZMK v0.3.0 supports `nice_nano_v2`; clone community reports | Clone pinout/charger variation | Measure board in Phase 1 |
| BLE split + USB HID | High | ZMK split and USB are mature | Multi-host/connection stability | Two-board BLE test |
| OLED + 10 s blank | High | ZMK display widgets; SSD1306 supported | Sleep current and burn-in | Breadboard OLED test |
| TrackPoint PS/2 | Medium | ZMK PS/2 module exists; module is 4-wire and low-profile | Protocol/reset/contact side unknown | Logic analyzer + breakout |
| Low profile 15–16 mm | Medium | Commercial Choc Corne ~15 mm; socketed MCU below keycaps | Battery pocket, case tolerances | Stack-up coupon and case v0.1 |
| 502030 battery + charging | High | nice!nano onboard charger; protected cell | Antenna keepout and case depth | Power/BLE measurement |
| Power budget / TrackPoint idle current | Medium | 250 mAh; ≥2 week target implies ~0.75 mA average | TrackPoint current unknown | Measure TrackPoint and sleep current in Phase 1 |
| Magnetic mount | High | 4x N52 + steel plate + camera ball head is a known pattern | Pull force, rotation, flat desk seating | Pull-force and mount prototype |
| ZMK Studio keymap | High | Official feature; Corne has a physical layout | Advanced features are partial | Baseline Studio build |
| Flutter configurator | Medium | ZMK Studio protocol is documented; Flutter supports BLE/serial | Protocol changes, custom RPC, DFU | Phase 4 MVP |
| Dongle | Medium | ZMK dongle support is documented | Extra build/board; latency | Phase 5 |
| Fingerprint | Medium | HLK-ZW0905 is UART, 3.3 V, 50 templates | Power peaks, privacy, no ready ZMK support | Phase 5 prototype |
| FIDO2/CTAP2 | Low–Medium | OpenSK runs on nRF52840; no fingerprint UV out of the box | Secure element, certification, architecture | Research ADR |
| Wired split | Medium | ZMK full-duplex UART is experimental | Protection, hot-plug, single transport | Phase 5 |

## Proven or low-risk

### Keyboard matrix and switches

The Corne 3x6+3 layout, Choc V1 switches, hot-swap sockets, and 1N4148W SOD-123 diodes are standard, well-understood parts. The only layout-specific work is fitting the TrackPoint and its flex into the right thumb cluster.

### Controller and ZMK

ZMK supports the nice!nano v2 and compatible clones. The clone is socketed, so a failed board can be replaced. The main unknown is the exact pinout/charger behavior of the Tenstar/SuperMini variant; Phase 1 measures it.

### BLE split and host connectivity

ZMK's BLE split and USB/BLE HID are mature. The v1 architecture keeps one transport active at a time and uses the right half as central because the TrackPoint is connected there. Multi-host BLE is supported.

### OLED

The SSD1306 128x32 is supported by ZMK. The display is off by default; the 10-second wake behavior is a small custom behavior. The only concern is sleep current, which is measured in Phase 1.

## Feasible with prototyping

### TrackPoint

The salvaged Dell module is a 4-wire FPC device with a black cap and a 0.5 mm pitch connector. It is likely PS/2. The ZMK PS/2 driver module exists, but TrackPoints often need a power-on-reset sequence. The module has only four wires, so the reset may be internal, a `0xFF` command may work, or a controlled VCC power-cycle may be needed.

**Plan:** build a breakout with top/bottom FPC footprints, pull-ups, and reset options; test with a logic analyzer; fall back to a known PS/2 module if necessary.

### Low profile

Commercial Choc Corne builds are about 15 mm with keycaps. The socketed controller sits at the top edge, outside the keycap field, so it does not have to increase the key area height. The battery pocket under the controller is the main variable. A 502030 cell is 5 mm thick; a local pocket can keep the key area at 15–16 mm. The final height is confirmed with a printed stack-up coupon.

### Magnetic mount

Four N52 magnets plus a 1 mm steel plate and a camera-style ball head is a standard quick-release pattern. The unknown is pull force vs weight and rotation during typing. A pull-force test and a 3D-printed mount prototype settle it.

### ZMK Studio

ZMK Studio supports runtime keymap editing over USB serial and BLE GATT. The Corne shield in ZMK main has a physical layout, so the baseline can enable Studio. Advanced features such as combos, macros, and tap dances are partial or planned. Custom settings (TrackPoint, display, power) need a custom RPC subsystem.

## Research or higher risk

### Fingerprint

The HLK-ZW0905 is a UART, 3.3 V capacitive sensor with match-in-sensor templates (about 50 slots) and 200 mA peaks. It can be integrated into a keyboard as a local unlock/verification input, but there is no ready ZMK module. It is not a FIDO2 authenticator by itself.

### FIDO2/CTAP2

FIDO2 on the keyboard controller is not a small feature. The nRF52840 is not a secure element. Feasible paths:

- Separate security MCU running OpenSK or a similar stack.
- Certified external security key integrated mechanically.
- Custom biometric bridge with a match-in-sensor module.

Serious use requires a threat model, secure key storage, attestation, and possibly certification. This is Phase 5 research, not v1.

### Flutter configurator

The ZMK Studio protocol is documented (protobuf + serial/GATT), but there is no official Flutter SDK. A Flutter client is feasible: protobuf generation, BLE via a Flutter plugin, serial via platform APIs. The hard parts are advanced settings and DFU, which are not part of ZMK Studio. The app is phased: keymap first, then settings/DFU.

### Wired split

ZMK supports full-duplex wired UART as an experimental feature. It needs two data wires plus power/ground and protection against hot-plug/backfeed. It is not needed for v1 and is deferred.

### Dongle

ZMK supports a dongle as a central with no keys. It adds a third board and a build target. It can improve battery life and connection stability, but it is not required for v1.

## Effort estimate

These are rough relative estimates, not schedule commitments.

| Work package | Effort | Notes |
|---|---|---|
| Phase 0 docs/automation | Small–medium | This package |
| Breadboard matrix/OLED | Small | Standard ZMK |
| TrackPoint breakout/test | Medium | Protocol/reset unknown |
| PCB schematic/layout | Medium–large | Two mirrored boards, new footprints |
| Case design/printing | Medium | Several iterations |
| Firmware integration | Medium | TrackPoint module, display behavior, Studio |
| Final acceptance | Medium | Measurements and fixes |
| Flutter app MVP | Medium–large | Protocol + BLE/serial + UI |
| App advanced settings/DFU | Large | Custom RPC + platform work |
| Fingerprint/FIDO2 | Large/research | Separate architecture |

## Go/no-go criteria

- **Go to PCB v0.1** when the matrix, OLED, TrackPoint (or fallback), and BLE split are proven on the breadboard.
- **Go to final PCB** when PCB v0.1 passes all keys, TrackPoint, display, battery, and RF checks.
- **Go to app expansion** when the final keyboard and ZMK Studio keymap editing are stable.
- **Go to fingerprint/FIDO2** only after a security ADR defines the threat model and architecture.
