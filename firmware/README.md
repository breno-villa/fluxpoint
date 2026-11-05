# Firmware

Fluxpoint uses **ZMK/Zephyr** with custom modules where ZMK does not provide a feature.

## Structure

| Path | Contents |
|---|---|
| `zmk-config/` | ZMK user config, baseline keymap, build manifest |
| `modules/` | Custom Zephyr modules (TrackPoint, display behavior, future settings) |
| `dongle/` | Future dongle firmware (Phase 5) |

## Current status

The `zmk-config/` baseline builds the in-tree Corne shield for tooling and breadboard bring-up. It is **not** the final Fluxpoint shield:

- The baseline is left-central, matching the stock Corne shield.
- The final firmware will be **right-central**, because the TrackPoint is on the right half.
- The baseline does not include the TrackPoint module; that is added in Phase 2.
- The baseline enables ZMK Studio for runtime keymap testing.

## Build and flash

The CI workflow and the command in [Automation](../docs/automation.md) build the baseline. Copy the resulting `.uf2` to the controller's UF2 mount:

1. Double-tap reset to enter the bootloader.
2. Copy `settings_reset` first if the controller has stale settings.
3. Copy the left/right firmware.
4. Reconnect and pair.

## Final firmware plan

- Custom `fluxpoint_left`/`fluxpoint_right` shield with the project matrix/pin map.
- Right half central; left half peripheral.
- TrackPoint PS/2 driver module, pinned to a tested ZMK fork revision.
- 10-second OLED wake behavior.
- ZMK Studio enabled on the central; unlock binding.
- Future custom RPC for TrackPoint/display/power settings.
- Flutter configurator uses the ZMK Studio protocol.

## TODO

- [x] Baseline CI build green
- [ ] 10-second display behavior
- [ ] TrackPoint module integration
- [ ] Custom shield and pin map
- [ ] Right-central split role
- [ ] ZMK Studio physical layout for Fluxpoint
- [ ] Flutter configurator (Phase 3)
