# ADR 0003: Connectivity and split roles

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [Layout](../layout.md), [TrackPoint](../trackpoint.md)

## Context

ZMK supports BLE split and USB/BLE host output. Full-duplex wired split is experimental and needs two UART wires plus protection. The TrackPoint is on the right half, and ZMK pointing devices must be connected to the central side. The default Corne central is the left half.

## Decision

- v1 uses BLE split between halves.
- The **right half is the central** because it carries the TrackPoint and OLED. The left half is the peripheral.
- The right half's USB-C port is the host/data port; the left half's USB-C port is for charging and flashing.
- Host connectivity: USB HID and BLE HID, including multi-host BLE.
- No wired split and no dongle in v1. Both remain future options; the firmware/build structure must not prevent them.
- ZMK Studio is enabled on the central; the unlock binding is available in the keymap.

## Consequences

- The TrackPoint works without routing its signals across the split link.
- The right half must be the one connected to the host for USB; this is a usability change from the usual left-central Corne.
- The left half still needs a controller, battery, and charging port.
- A future dongle can become the central, but the TrackPoint would then need to be on the dongle or the split role/driver behavior must change; this is a Phase 5 design issue.
