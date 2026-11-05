# ADR 0002: Controller and firmware base

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [Requirements](../requirements.md)

## Context

The builder already owns four Tenstar/SuperMini nice!nano v2 clones (nRF52840). ZMK supports the nice!nano v2 and provides BLE split, USB HID, displays, and pointing-device support. A fully custom bare nRF52840 module would reduce height but require RF/antenna design and a new board.

## Decision

- Use the nice!nano clone on both halves, socketed with 2.54 mm headers.
- Use ZMK/Zephyr as the firmware base, with custom modules only where ZMK lacks support (TrackPoint, display behavior, future settings).
- Keep the controller at the top edge, outside the keycap field, so its socket height does not dictate the key area height.
- The baseline firmware uses the in-tree Corne shield for tooling/bring-up; the final firmware uses a custom Fluxpoint shield.

## Consequences

- Lower electrical/RF risk and faster bring-up.
- The controller is replaceable; a failed clone does not scrap the PCB.
- The socketed controller needs a case cutout and a local top-edge clearance.
- A future bare-module revision remains possible if the socket height or cost becomes a problem.
