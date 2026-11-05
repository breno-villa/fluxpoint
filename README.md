# Fluxpoint

Fluxpoint is a low-profile split keyboard based on the Corne 3x6+3 layout. It combines a Kailh Choc V1 matrix, a socketed nice!nano-class controller, a salvaged TrackPoint, a small OLED, a rechargeable battery per half, and a magnetic mounting interface for desk, chair-arm, and travel use.

> **Status:** Phase 0 — skeleton, requirements, ADRs, and automation. This repository is still a working specification. Hardware and firmware are not final.

## At a glance

| Area | Current direction |
|---|---|
| Layout | Corne 3x6+3, 42 keys, QWERTY base + layers |
| Switches | Kailh Choc V1, hot-swap, 1N4148W SOD-123 diodes |
| Controller | Tenstar/SuperMini nice!nano v2 clone, socketed |
| Firmware | ZMK + modules; ZMK Studio enabled for runtime keymap editing |
| Connectivity | BLE split + USB/BLE HID to host; no wired split in v1 |
| Pointing | Salvaged Dell TrackPoint, PS/2, right thumb cluster |
| Display | 0.91" 128x32 SSD1306 OLED now; nice!view footprint in the final PCB |
| Power | 502030 250 mAh LiPo per half, USB-C charging, slide switch |
| Mechanical | 3D-printed case, FR4 switch plate, 4x N52 magnets + steel plate + 1/4"-20 ball head |
| Keycaps | MBK blank, Choc V1 |
| Target height | 15–16 mm with keycaps |
| Target autonomy | 2–4 weeks with OLED off and the documented TrackPoint power policy |
| Configurator | Flutter app, Phase 4, monorepo at `software/configurator` |
| Licenses | Hardware CERN-OHL-S-2.0, firmware MIT, docs CC BY 4.0 |

## Documentation

Start with the [documentation index](docs/README.md).

- [Requirements](docs/requirements.md)
- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Feasibility](docs/feasibility.md)
- [BOM and inventory](docs/bom.md)
- [Bring-up and acceptance tests](docs/bringup.md)
- [Automation and MCPs](docs/automation.md)
- [TrackPoint integration](docs/trackpoint.md)
- [Layout and keymap](docs/layout.md)
- [Architecture decision records](docs/decisions/README.md)

## Repository layout

```text
.
├── docs/                  # requirements, architecture, roadmap, ADRs, BOM, bring-up
├── hardware/              # PCB, case, diagrams, TrackPoint notes
├── firmware/              # ZMK config, custom modules, dongle
├── software/              # Flutter configurator (Phase 4)
├── tools/                 # automation CLI and tests
├── .github/workflows/     # CI and baseline firmware build
└── .opencode/skills/      # project-specific agent skills
```

## Quick start

The current baseline firmware is a standard Corne shield for ZMK bring-up. It is intentionally not the final Fluxpoint shield.

```bash
# Documentation and tool checks
python tools/fluxpoint_cli.py check-docs
python tools/fluxpoint_cli.py check-config
python -m pytest -q tools/tests

# Build the baseline firmware locally (requires Docker)
docker run --rm -v "$PWD:/workspace" -w /workspace/firmware/zmk-config \
  zmkfirmware/zmk-build-arm:stable bash -lc '
    west init -l config
    west update --narrow --group-filter=-optional
    west build -s zmk/app -d build/left -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=corne_left \
      -DSNIPPET=studio-rpc-usb-uart -DCONFIG_ZMK_STUDIO=y
  '
```

Flash the resulting `firmware/zmk-config/build/left/zephyr/zmk.uf2` by copying it to the controller's UF2 mount.

## Design phase

This project is milestone-based, not date-based. Phase 0 closes the documentation and tooling. Phase 1 validates the riskiest pieces on a breadboard before any custom PCB is ordered. See the [roadmap](docs/roadmap.md).

## Contributing

The project is public and open hardware. Keep changes consistent with the [ADRs](docs/decisions/README.md), run the documentation and tool checks before opening a pull request, and do not add generated fabrication files to the repository.

## License and attribution

- Hardware: [CERN-OHL-S-2.0](LICENSE/CERN-OHL-S-2.0.txt)
- Firmware: [MIT](LICENSE/MIT.txt)
- Documentation: [CC BY 4.0](LICENSE/CC-BY-4.0.txt)

The Corne layout and reference files are by foostan and contributors, licensed MIT and CC BY 4.0. See [NOTICE](NOTICE) for attribution. The salvaged TrackPoint and other third-party parts remain subject to their own terms.
