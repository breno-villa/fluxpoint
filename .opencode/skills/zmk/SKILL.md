---
name: zmk
description: Use when working on Fluxpoint ZMK firmware, keymaps, custom shields, ZMK Studio, split roles, TrackPoint driver integration, build failures, or flashing.
---

# ZMK workflow

Read `firmware/README.md`, `firmware/zmk-config/README.md`, `docs/layout.md`, and `docs/architecture.md` before changing firmware.

## Current baseline

- `firmware/zmk-config` builds the in-tree Corne shield.
- Baseline is **left-central** (stock Corne); the final Fluxpoint firmware is **right-central** because the TrackPoint is on the right half.
- Baseline has no TrackPoint; it is a matrix/OLED/Studio bring-up image.
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
    west init -l config
    west update
    west build -s zmk/app -d build/left -b nice_nano_v2 -- \
      -DZMK_CONFIG=$PWD/config -DSHIELD=corne_left \
      -DSNIPPET=studio-rpc-usb-uart
  '
```

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
- ZMK pointing devices must be on the central side; the right half is central.
- Test reset via `0xFF`, RC, and MOSFET power-cycle.

## Rules

- Do not guess pins.
- Keep keymap binding counts equal to 42 per layer.
- Validate with CI before merging.
- Document fork/module revisions in `west.yml`.
- Human review before flashing a new board.
