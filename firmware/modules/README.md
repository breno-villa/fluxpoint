# Custom modules

Planned Phase 2 modules:

- TrackPoint PS/2 integration (may use `kb_zmk_ps2_mouse_trackpoint_driver`).
- 10-second OLED wake behavior.
- Runtime TrackPoint/display/power settings (custom ZMK Studio RPC).
- Optional split-role helper for the right-central configuration.

Each module must have:

- a `west.yml`-compatible manifest or be vendored with a pinned revision;
- a README with build/config instructions;
- a CI build target;
- a license compatible with the project.

No module is implemented in Phase 0.
