# ADR 0001: Project scope and v1 MVP

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Requirements](../requirements.md), [Roadmap](../roadmap.md)

## Context

The project vision includes a split keyboard, TrackPoint, OLED, wireless split, dongle, fingerprint, FIDO2, wired split, and a Flutter configurator. Trying to deliver all of it in the first hardware revision would multiply firmware, security, and mechanical risk. The available budget is R$ 500–1,500, the timeline is open, and the builder is returning to electronics after a long break.

## Decision

v1 is a 42-key Corne 3x6+3 split keyboard with:

- Kailh Choc V1 hot-swap switches and a socketed nice!nano clone;
- BLE split and USB/BLE host connectivity;
- the salvaged Dell TrackPoint in the right thumb cluster;
- a 0.91" SSD1306 OLED with a 10-second wake;
- a 502030 250 mAh battery per half;
- a 3D-printed case with a magnetic N52/steel-plate/ball-head mount.

Dongle, fingerprint, FIDO2/CTAP2, wired split, and the Flutter app are deferred to later phases. The right PCB reserves a fingerprint header and load switch, and the firmware is structured so a dongle can be added later.

## Consequences

- The first usable keyboard can be validated before security and dongle work.
- The TrackPoint remains the main technical risk; it is tested on a breadboard first.
- The future fingerprint/FIDO2 architecture is not constrained by v1, but the expansion header is available.
- The project can ship a working open-hardware keyboard without waiting for a FIDO2 certification effort.
