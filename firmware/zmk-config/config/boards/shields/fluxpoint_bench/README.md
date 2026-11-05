# fluxpoint_bench

Phase 1 breadboard shield. **Not the final Fluxpoint shield.**

- Right half is central; left half is peripheral.
- 4x6 matrix with 21 populated positions per half, `col2row`.
- OLED on the right half only (I2C, `0x3C`).
- Candidate pins from [`docs/pinmap.md`](../../../../../../docs/pinmap.md); they are not frozen.
- TrackPoint is not wired into this shield yet. D0/D1 are the preferred UART candidates and D8/D9 are reserved for reset/load-switch work.

## Build

```bash
docker run --rm -v "$PWD:/workspace" -w /workspace/firmware/zmk-config \
  zmkfirmware/zmk-build-arm:stable bash -lc '
    west build -s zmk/app -d build/bench-right -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=fluxpoint_bench_right \
      -DSNIPPET=studio-rpc-usb-uart
  '
```

Use `west update` instead of `west init -l config` if the workspace already exists.

## Files

- `fluxpoint_bench.dtsi` — shared matrix, transform, and kscan.
- `fluxpoint_bench_left.overlay` — left column pins, peripheral.
- `fluxpoint_bench_right.overlay` — right column pins, central, OLED.
- `fluxpoint_bench_left.conf` / `fluxpoint_bench_right.conf` — per-half Kconfig (split shields do not pick up a shared conf from this folder).
- `fluxpoint_bench.keymap` — temporary 42-key Corne keymap.
- `fluxpoint_bench.zmk.yml` — shield metadata.
