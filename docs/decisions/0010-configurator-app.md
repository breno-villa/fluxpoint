# ADR 0010: Flutter configurator

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [Roadmap](../roadmap.md)

## Context

The builder wants to configure the keyboard after it is assembled without rebuilding firmware, including keys. ZMK Studio already provides runtime keymap editing over USB serial and BLE GATT, but its official app is not Flutter. The ZMK Studio protocol is documented (protobuf + transports), and advanced settings/DFU are outside its current scope.

## Decision

- Enable ZMK Studio in the v1 firmware.
- Build a Flutter configurator in Phase 4, in the monorepo at `software/configurator`.
- Targets: Android, Linux, Windows, macOS.
- MVP: keymap/layers, keycodes/behaviors, import/export, local profiles.
- Later: combos, macros, tap dances, TrackPoint/display/power settings, BLE profiles, DFU, diagnostics.
- Use the documented ZMK Studio protobuf messages and transports; use custom RPC modules for settings that Studio does not expose.
- Do not block hardware delivery on the app; ZMK Studio is the interim editor.

## Consequences

- The app is a significant Phase 4 project, not a v1 dependency.
- Advanced settings require custom ZMK RPC work and version compatibility.
- The app can reuse the official protocol and avoid a proprietary configuration format.
- The firmware must include a physical layout and a Studio unlock binding.
