# ZMK config and Phase 1 bench shield

This directory is the Phase 0/1 ZMK user config. It builds the stock Corne shield for tooling validation and the `fluxpoint_bench_left`/`fluxpoint_bench_right` shield for breadboard bring-up. The bench shield is **right-central**, matches the final split architecture, and uses the candidate pin map in [`docs/pinmap.md`](../../docs/pinmap.md). Neither shield is the final Fluxpoint shield.

## Files

| File | Purpose |
|---|---|
| `build.yaml` | Build targets for Corne, the Phase 1 bench shield, and settings-reset |
| `config/west.yml` | ZMK manifest |
| `config/corne.keymap` | Corne QWERTY + lower/raise/adjust layers; Studio unlock |
| `config/corne.conf` | Display, sleep, ZMK Studio settings |
| `config/boards/shields/fluxpoint_bench/` | Phase 1 bench shield: matrix, OLED, right-central split |

## Important limitations

- The stock Corne shield is **left-central**. The Phase 1 bench shield and the final Fluxpoint firmware are **right-central** because the TrackPoint is on the right half.
- The bench shield has the matrix and OLED, but no TrackPoint support yet; it uses candidate pins from `docs/pinmap.md`, not a frozen map.
- The ZMK revision is pinned to `v0.3.0`. Re-test before moving to a newer release.
- The final custom shield will replace the bench shield and use the frozen Fluxpoint matrix/pin map.

## Build locally

If the workspace is already initialized (`firmware/zmk-config/.west` exists), use `west update` instead of `west init -l config`.

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
    west build -s zmk/app -d build/bench-left -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=fluxpoint_bench_left
    west build -s zmk/app -d build/bench-right -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=fluxpoint_bench_right \
      -DSNIPPET=studio-rpc-usb-uart
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
4. Power both halves and pair the central to the host. The Corne baseline is left-central; the Phase 1 bench shield is right-central, matching the final design.

## Keymap

The baseline uses the default Corne QWERTY layout plus:

- Lower layer: numbers, Bluetooth profiles, arrows.
- Raise layer: symbols.
- Adjust layer: Studio unlock, Bluetooth clear, system reset, bootloader. Press both outer thumb keys to activate the adjust layer.
- ZMK Studio unlock is also available on the adjust layer.

See [Layout](../../docs/layout.md) for the intended Fluxpoint layout.

## Next steps

- [x] Pin the ZMK revision (v0.3.0)
- [x] Add the Phase 1 bench shield (matrix + OLED, right-central)
- [ ] Verify the clone pin map and freeze `docs/pinmap.md`
- [ ] Add the TrackPoint module/fork
- [ ] Create the final Fluxpoint shield
- [ ] Add the 10-second OLED behavior
- [ ] Add the Flutter configurator integration
