# Firmware

Fluxpoint uses **ZMK/Zephyr** with custom modules where ZMK does not provide a feature.

## Structure

| Path | Contents |
|---|---|
| `zmk-config/` | ZMK user config, baseline keymap, build manifest |
| `modules/` | Custom Zephyr modules (TrackPoint, display behavior, future settings) |
| `dongle/` | Future dongle firmware (Phase 5) |

## Current status

The `zmk-config/` baseline builds the in-tree Corne shield for tooling validation and the Phase 1 `fluxpoint_bench_left`/`fluxpoint_bench_right` shield for breadboard bring-up. Neither is the final Fluxpoint shield:

- The Corne baseline is left-central, matching the stock shield.
- The bench shield is **right-central**, matching the final architecture; it uses the candidate pin map in [`docs/pinmap.md`](../docs/pinmap.md).
- The bench shield has the matrix and OLED; it does **not** include the TrackPoint module yet.
- Both enable ZMK Studio for runtime keymap testing.

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
- [x] Phase 1 bench shield (matrix + OLED, right-central)
- [ ] 10-second display behavior
- [ ] TrackPoint module integration
- [ ] Custom shield and frozen pin map
- [ ] Right-central final split role
- [ ] ZMK Studio physical layout for Fluxpoint
- [ ] Flutter configurator (Phase 4)
