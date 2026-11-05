# Automation, MCPs, and skills

- **Status:** Phase 0 baseline
- **Last updated:** 2026-11-05
- **Related:** [Roadmap](roadmap.md), [BOM](bom.md), [Bring-up](bringup.md)

## 1. Goals

Automate the repeatable parts of the project:

- documentation and link/config validation;
- firmware build, artifact packaging, and release notes;
- KiCad schematic/PCB inspection, ERC/DRC, BOM, and fabrication exports;
- FreeCAD/OpenSCAD case and plate iteration;
- bench serial logging, logic capture, and power measurements;
- BOM checks and procurement notes.

The agent proposes and executes; a human reviews every schematic, PCB, mechanical, and safety-critical change.

## 2. Local toolchain

The development machine is Arch Linux. Install the core tools with the setup script:

```bash
./tools/setup_dev.sh
```

Equivalent manual command:

```bash
sudo pacman -S --needed \
  kicad freecad openscad \
  arm-none-eabi-gcc probe-rs openocd \
  sigrok-cli python-pyserial python-yaml \
  python-pytest
```

Already available: `git`, `gh`, `docker`, `podman`, `uv`, `node`, `npm`, `bun`, `cargo`, `west`, `nrfutil`.

Optional: `pulseview` for the logic analyzer GUI, `kicad-cli` is provided by the `kicad` package, and `pyvisa` if a SCPI bench supply is used.

## 3. MCP servers

MCP servers are optional accelerators. Configure them in `~/.config/opencode/opencode.json` under `mcp.servers`.

### 3.1 KiCad — Konnect

Konnect is a KiCad 10 native plugin and MCP server. The original `mixelpixx/Konnect` repository is archived and AGPL-3.0; development continues in Konnect-EDA, which is free for hobby, student, and open-hardware work but commercial for businesses. The older [KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server) remains MIT and is the fallback.

1. Download the standalone Linux server binary from the Konnect releases page.
2. Install the KiCad plugin package if you want the in-editor UI.
3. Point OpenCode at the server binary:

```json
{
  "mcp": {
    "servers": {
      "kicad": {
        "type": "local",
        "command": ["/home/breno/.local/bin/konnect-server"]
      }
    }
  }
}
```

Replace the path with the actual binary. Verify with a small test project before using it on the real board. Always review ERC/DRC output and fabrication files manually.

### 3.2 FreeCAD

FreeCAD MCP has two parts: an addon inside FreeCAD and a server process.

```bash
git clone https://github.com/neka-nat/freecad-mcp.git
# copy addon/FreeCADMCP into the FreeCAD addon directory
# restart FreeCAD, open the MCP Addon workbench, start the RPC server
```

```json
{
  "mcp": {
    "servers": {
      "freecad": {
        "type": "local",
        "command": ["uvx", "freecad-mcp"]
      }
    }
  }
}
```

FreeCAD must be open with the RPC server running while the MCP is used.

### 3.3 OpenSCAD

```json
{
  "mcp": {
    "servers": {
      "openscad": {
        "type": "local",
        "command": ["uvx", "openscad-mcp"],
        "environment": {
          "OPENSCAD_PATH": "/usr/bin/openscad"
        }
      }
    }
  }
}
```

### 3.4 REA

The `rea` MCP is already configured in this environment. It is useful for reverse-engineering firmware binaries, inspecting protocols, and analyzing captured data. It is optional for Fluxpoint; use it only when static analysis adds value.

### 3.5 GitHub

The `gh` CLI is authenticated. Use it for issues, pull requests, releases, and workflow runs. A GitHub MCP is optional; the CLI is sufficient for this repository.

## 4. Project skills

Skills live in `.opencode/skills/` and are loaded by OpenCode when their descriptions match the task.

| Skill | Use |
|---|---|
| `fluxpoint` | Project overview, conventions, links, current phase |
| `kicad` | KiCad/Konnect workflow, ERC/DRC, BOM, Gerber |
| `zmk` | ZMK build/flash/modules/keymap/Studio |
| `cad` | FreeCAD/OpenSCAD case, plate, magnets, print settings |
| `bringup` | Bench safety, TrackPoint test, logic capture, power |
| `bom` | Inventory, procurement, suppliers, cost |
| `docs` | Requirements, ADRs, roadmap, link/config checks |

Skills should point to the docs rather than duplicate them. Update a skill when the workflow changes.

## 5. CI

### 5.1 Documentation and tools

`.github/workflows/ci.yml` runs on push, pull request, and manual dispatch:

- `python tools/fluxpoint_cli.py check-docs`
- `python tools/fluxpoint_cli.py check-config`
- `python -m pytest -q tools/tests`

### 5.2 Baseline firmware

`.github/workflows/firmware.yml` builds the baseline Corne configuration in the ZMK ARM container and uploads the UF2 artifacts. It is a tooling/bring-up baseline, not the final Fluxpoint shield.

### 5.3 Future jobs

- KiCad ERC/DRC and fabrication export.
- FreeCAD/OpenSCAD STL/STEP export and bounding-box checks.
- Flutter analyze/test/build.
- Release packaging and checksums.

## 6. Automation CLI

`tools/fluxpoint_cli.py` has no required third-party dependency for the documentation/config checks. Hardware commands import optional dependencies lazily.

```bash
# Validate Markdown links
python tools/fluxpoint_cli.py check-docs

# Validate YAML files
python tools/fluxpoint_cli.py check-config

# Run tests
python -m pytest -q tools/tests

# Flash a UF2 to a mounted bootloader volume
python tools/fluxpoint_cli.py flash --uf2 build/left/zephyr/zmk.uf2 --mount /media/$USER/NICENANO

# Log a serial console
python tools/fluxpoint_cli.py serial --port /dev/ttyACM0 --baud 115200 --log serial.log

# Capture with sigrok-cli
python tools/fluxpoint_cli.py logic --driver fx2lafw --channels D0,D1 --time 2s --output capture.sr

# SCPI power measurement (optional)
python tools/fluxpoint_cli.py power --resource USB0::0x1234::0x5678::INSTR --measure current
```

## 7. Firmware build

Local baseline:

```bash
docker run --rm -v "$PWD:/workspace" -w /workspace/firmware/zmk-config \
  zmkfirmware/zmk-build-arm:stable bash -lc '
    west init -l config
    west update --narrow --group-filter=-optional
    west build -s zmk/app -d build/left -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=corne_left \
      -DSNIPPET=studio-rpc-usb-uart -DCONFIG_ZMK_STUDIO=y
    west build -s zmk/app -d build/right -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=corne_right -DCONFIG_ZMK_STUDIO=y
    west build -s zmk/app -d build/reset -b nice_nano_v2 -- \
      -DZephyr_DIR=$PWD/zephyr/share/zephyr-package/cmake \
      -DZMK_CONFIG=$PWD/config -DSHIELD=settings_reset
  '
```

The final firmware will replace the in-tree Corne shield with a custom `fluxpoint` shield and add the TrackPoint module.

## 8. Human review gates

Automation does not replace engineering review. A human must review:

- schematic and PCB before fabrication;
- ERC/DRC reports and any suppressions;
- battery/charger/backfeed protection;
- TrackPoint power/reset wiring;
- case clearances, magnet polarity, and antenna keepout;
- firmware pin maps and matrix transforms;
- release artifacts and licenses.

## 9. Limitations

- Konnect-EDA is commercial after 1.0 for businesses; the old Konnect is AGPL-3.0. The fallback KiCAD-MCP-Server is MIT.
- FreeCAD/OpenSCAD MCPs are experimental and depend on the local CAD version.
- ZMK Studio supports keymaps well; combos/macros/tap dances and custom settings are partial.
- The app's advanced settings require custom RPC modules.
- CI cannot validate RF, battery safety, or mechanical fit; those require bench tests.
- The baseline firmware is a Corne shield, not the final Fluxpoint hardware.
