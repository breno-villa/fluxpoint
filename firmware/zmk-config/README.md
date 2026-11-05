# ZMK baseline config

This directory is the Phase 0/1 ZMK user config. It builds the stock Corne shield with a simple QWERTY keymap, ZMK Studio, and an OLED display. It exists to validate the toolchain and the breadboard matrix before the custom Fluxpoint shield exists.

## Files

| File | Purpose |
|---|---|
| `build.yaml` | Build targets for left, right, and settings-reset |
| `config/west.yml` | ZMK manifest |
| `config/corne.keymap` | QWERTY + lower/raise/adjust layers; Studio unlock |
| `config/corne.conf` | Display, sleep, ZMK Studio settings |

## Important limitations

- The stock Corne shield is **left-central**. The final Fluxpoint firmware is **right-central** because the TrackPoint is on the right half.
- The baseline has no TrackPoint support; it is a matrix/OLED/Studio bring-up image.
- The ZMK revision is pinned to `v0.3.0`. Re-test before moving to a newer release.
- The final custom shield will replace `corne_left`/`corne_right` and use the Fluxpoint matrix/pin map.

## Build locally

```bash
docker run --rm -v "$PWD/../..:/workspace" -w /workspace/firmware/zmk-config \
  zmkfirmware/zmk-build-arm:stable bash -lc '
    west init -l config
    west update --narrow --group-filter=-optional
    west build -s zmk/app -d build/left -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=corne_left \
      -DSNIPPET=studio-rpc-usb-uart
    west build -s zmk/app -d build/right -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=corne_right
    west build -s zmk/app -d build/reset -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=settings_reset
  '
```

The resulting UF2 files are under `build/*/zephyr/zmk.uf2`.

## Flashing

1. Double-tap the controller reset button; a `NICENANO`-style USB volume appears.
2. Copy `settings_reset` first if the controller has old settings.
3. Copy the left and right images to their respective controllers.
4. Power both halves and pair the central (left, in this baseline) to the host.

## Keymap

The baseline uses the default Corne QWERTY layout plus:

- Lower layer: numbers, Bluetooth profiles, arrows.
- Raise layer: symbols.
- Adjust layer: Studio unlock, Bluetooth clear, system reset, bootloader. Press both outer thumb keys to activate the adjust layer.
- ZMK Studio unlock is also available on the adjust layer.

See [Layout](../../docs/layout.md) for the intended Fluxpoint layout.

## Next steps

- [x] Pin the ZMK revision (v0.3.0)
- [ ] Add the TrackPoint module/fork
- [ ] Create the custom Fluxpoint shield
- [ ] Switch the central role to the right half
- [ ] Add the 10-second OLED behavior
- [ ] Add the Flutter configurator integration
