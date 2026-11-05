# Layout and keymap

- **Status:** Phase 0 baseline
- **Last updated:** 2026-11-05
- **Related:** [Requirements](requirements.md), [Architecture](architecture.md), [TrackPoint](trackpoint.md)

## 1. Physical layout

Fluxpoint uses the Corne 3x6+3 layout: three rows of six keys per half, plus three thumb keys per half. Total: 42 keys.

```text
Left half                                   Right half
┌───┬───┬───┬───┬───┬───┐                   ┌───┬───┬───┬───┬───┬───┐
│Tab│ Q │ W │ E │ R │ T │                   │ Y │ U │ I │ O │ P │Bsp│
├───┼───┼───┼───┼───┼───┤                   ├───┼───┼───┼───┼───┼───┤
│Ctl│ A │ S │ D │ F │ G │                   │ H │ J │ K │ L │ ; │ ' │
├───┼───┼───┼───┼───┼───┤                   ├───┼───┼───┼───┼───┼───┤
│Sft│ Z │ X │ C │ V │ B │                   │ N │ M │ , │ . │ / │Esc│
└───┴───┴───┼───┼───┼───┤                   ├───┼───┼───┼───┴───┴───┘
            │GUI│LWR│Spc│                   │Ent│RSE│Alt│
            └───┴───┴───┘                   └───┴───┴───┘
                                            ▲
                                     TrackPoint in the
                                     right thumb cluster
```

- Key spacing: Choc 18 x 17 mm.
- Thumb cluster: three keys per side; the right cluster also hosts the TrackPoint below/next to the keys.
- The TrackPoint cap is operated by the right thumb; the right thumb keys provide left/right/middle click, either as dedicated keys or on a pointing layer.
- One thumb key (for example, the middle right thumb) enables the scroll layer while held.
- The baseline Corne keymap keeps Enter/Raise/Alt on the right thumb keys. The final Fluxpoint keymap must resolve how those base-layer functions coexist with clicks and scroll; this is an open layout question.

## 2. Base layer (QWERTY)

| Row | Left | Right |
|---|---|---|
| Top | Tab, Q, W, E, R, T | Y, U, I, O, P, Backspace |
| Home | Ctrl, A, S, D, F, G | H, J, K, L, Semicolon, Quote |
| Bottom | Shift, Z, X, C, V, B | N, M, Comma, Dot, Slash, Esc |
| Thumb | GUI, Lower, Space | Enter, Raise, Alt |

The baseline firmware in `firmware/zmk-config/config/corne.keymap` implements this layout with lower, raise, and adjust layers.

## 3. Lower layer

- Numbers 1–0 on the top row.
- Bluetooth profile selection and clear on the home row.
- Arrow keys on the right home row.
- Transparent keys elsewhere.

## 4. Raise layer

- Symbols on the top and home rows.
- Brackets, minus/equal, backslash, grave, and shifted symbols.
- Transparent keys elsewhere.

## 5. Adjust layer

The adjust layer is for system and maintenance actions. The baseline uses the lower layer plus a dedicated key for ZMK Studio unlock; the final keymap can use a combo or a fourth layer.

Suggested bindings:

- ZMK Studio unlock.
- Bluetooth clear.
- System reset.
- Bootloader.
- Battery/display status wake.
- Optional media keys.

## 6. Pointing device bindings

- TrackPoint movement: handled by the ZMK PS/2 input listener.
- Left/right/middle click: right thumb keys, either dedicated or on a pointing layer.
- Scroll: hold the scroll thumb key; vertical TrackPoint movement becomes wheel movement.
- Sensitivity/axis settings: key behaviors or custom Studio RPC in the final firmware.
- The TrackPoint is on the right half, and the **right half is the central** in the final firmware. The left half is the peripheral. v1 keeps the pointing device on the central side to avoid input-split forwarding; newer ZMK releases can forward a peripheral pointing device, but v1 does not rely on it.
- The right half's USB-C port is the host/data port; the left half's USB-C port is for charging and flashing.
- The baseline Corne firmware is left-central only because it uses the stock shield; the custom Fluxpoint shield will switch the central role to the right half.

## 7. Keymap editing

- Runtime: ZMK Studio over USB or BLE.
- Persistent: the keymap is stored in the controller's settings; a "restore stock settings" action resets it.
- The final Flutter app will provide a graphical editor, import/export, and advanced settings.
- The baseline keymap is intentionally simple; the layout and layers will be tuned after the breadboard and first PCB.

## 8. Open layout questions

- Exact thumb cluster angle and spacing.
- TrackPoint position vs thumb key travel.
- How the three right thumb keys provide base-layer keys, mouse clicks, and scroll.
- Scroll key choice.
- Whether to use a combo for the adjust layer.
- Keycap legends (MBK blank assumed).
- Final thumb cluster angle and TrackPoint clearance.
