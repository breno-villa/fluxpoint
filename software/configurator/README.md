# Fluxpoint configurator

Flutter app for configuring Fluxpoint after assembly, without rebuilding firmware.

## Status

Phase 3. No Flutter code yet. ZMK Studio is the interim keymap editor.

## Targets

- Android
- Linux
- Windows
- macOS

## Transport

- USB CDC serial (ZMK Studio serial transport)
- BLE GATT (ZMK Studio custom service)

## Scope

### MVP

- Connect/disconnect over USB and BLE.
- Read and edit keymap/layers.
- Assign keycodes and predefined/user behaviors.
- Import/export keymap and local profiles.
- Unlock ZMK Studio.
- Device/battery/status readout.

### Advanced

- Combos, macros, tap dances (where ZMK Studio supports them; otherwise custom RPC).
- TrackPoint sensitivity, axis, scroll, and reset settings.
- Display timeout and wake behavior.
- Power/deep-sleep settings.
- BLE profile management.
- DFU/firmware update.
- Diagnostics: matrix test, logs, battery history.

## Architecture

- Flutter UI + platform plugins for BLE and serial.
- Protobuf definitions from `zmk-studio-messages`.
- A generated Dart protocol layer.
- Custom RPC subsystem for Fluxpoint settings.
- Mock device/server for tests.

## CI

- `flutter analyze`
- `flutter test`
- Platform builds for Android/Linux/Windows/macOS.

## Risks

- ZMK Studio protocol changes.
- BLE permissions and platform restrictions.
- DFU complexity and recovery.
- Custom RPC version compatibility.
- App scope creep; keep the hardware-independent MVP first.
