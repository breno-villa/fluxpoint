---
name: zmk
description: Use when working on Fluxpoint ZMK firmware, keymaps, custom shields, ZMK Studio, split roles, TrackPoint driver integration, build failures, or flashing.
---

# ZMK workflow

Read `firmware/README.md`, `firmware/zmk-config/README.md`, `docs/layout.md`, and `docs/architecture.md` before changing firmware.

## Current baseline

- `firmware/zmk-config` builds the in-tree Corne shield and the Phase 1 `fluxpoint_bench_left`/`fluxpoint_bench_right` shield.
- The Corne baseline is **left-central**; the Phase 1 bench shield and the final Fluxpoint firmware are **right-central** because the TrackPoint is on the right half.
- The bench shield has the matrix and OLED; it has no TrackPoint node yet. Its pins are candidates from `docs/pinmap.md`, not a frozen map.
- `config/corne.keymap` has QWERTY, lower, raise, adjust, and a Studio unlock binding.
- `config/corne.conf` enables display, sleep, and ZMK Studio.

## Final firmware plan

- Custom `fluxpoint_left`/`fluxpoint_right` shield.
- Right half central, left half peripheral.
- Matrix/pin map from the schematic, not guessed.
- TrackPoint PS/2 module pinned to a tested ZMK fork/module revision.
- 10-second OLED wake behavior.
- ZMK Studio enabled on the central; physical layout node required.
- Custom RPC for TrackPoint/display/power settings later.

## Build

```bash
docker run --rm -v "$PWD:/workspace" -w /workspace/firmware/zmk-config \
  zmkfirmware/zmk-build-arm:stable bash -lc '
    west update
    west build -s zmk/app -d build/bench-right -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=fluxpoint_bench_right \
      -DSNIPPET=studio-rpc-usb-uart
  '
```

Use `west init -l config` only on a fresh workspace; after the first build, run `west update` instead.

## Flash

```bash
python tools/fluxpoint_cli.py flash --uf2 build/left/zephyr/zmk.uf2 --label nicenano
```

Double-tap reset; copy `settings_reset` first if settings are stale.

## ZMK Studio

- Enable `CONFIG_ZMK_STUDIO=y` and the `studio-rpc-usb-uart` snippet on the central.
- Add `&studio_unlock` to the keymap.
- The custom shield must define a physical layout with `keys` and must not have a chosen matrix transform conflict.
- Studio edits persist in settings; "restore stock settings" resets them.

## TrackPoint

- Use `kb_zmk_ps2_mouse_trackpoint_driver` or equivalent.
- It currently depends on a ZMK fork with mouse support; pin a tested revision.
- Prefer UART driver on nRF52; GPIO is fallback.
- v1 keeps the TrackPoint on the central side (right half); newer ZMK input split can forward peripheral pointing devices, but v1 does not rely on it.
- Test reset via `0xFF`, RC, and MOSFET power-cycle.

## Rules

- Do not guess pins.
- Keep keymap binding counts equal to 42 per layer.
- Validate with CI before merging.
- Document fork/module revisions in `west.yml`.
- Human review before flashing a new board.
