#!/usr/bin/env bash
# Fluxpoint development setup for Arch Linux.
# Installs the system packages used by the documented toolchain.
# It does not edit your OpenCode config automatically; it prints the MCP snippet.

set -euo pipefail

if ! command -v pacman >/dev/null 2>&1; then
  echo "This script targets Arch Linux (pacman). Install the equivalent packages manually." >&2
  exit 1
fi

if ! command -v uvx >/dev/null 2>&1; then
  echo "warning: uv/uvx not found; install it for the FreeCAD/OpenSCAD MCP servers." >&2
fi

echo "Installing Fluxpoint development packages (sudo may prompt for a password)..."
sudo pacman -S --needed \
  kicad freecad openscad \
  arm-none-eabi-gcc probe-rs openocd \
  sigrok-cli python-pyserial python-yaml python-pytest

cat <<'EOF'

System packages installed.

Python/tool checks:
  python tools/fluxpoint_cli.py check-docs
  python tools/fluxpoint_cli.py check-config
  python -m pytest -q tools/tests

MCP servers to add to ~/.config/opencode/opencode.json:

{
  "mcp": {
    "servers": {
      "kicad": {
        "type": "local",
        "command": ["/home/breno/.local/bin/konnect-server"]
      },
      "freecad": {
        "type": "local",
        "command": ["uvx", "freecad-mcp"]
      },
      "openscad": {
        "type": "local",
        "command": ["uvx", "openscad-mcp"],
        "environment": { "OPENSCAD_PATH": "/usr/bin/openscad" }
      }
    }
  }
}

Konnect:
  Download the standalone server binary from the Konnect releases page and
  replace the path above. Konnect-EDA is the successor; the archived Konnect
  repo is AGPL-3.0. KiCAD-MCP-Server (MIT) is the fallback.

FreeCAD:
  Clone https://github.com/neka-nat/freecad-mcp, copy addon/FreeCADMCP into
  the FreeCAD addon directory, restart FreeCAD, open the MCP Addon workbench,
  and start the RPC server before using the MCP.

OpenSCAD:
  The MCP is launched via `uvx openscad-mcp`; OpenSCAD must be on PATH.

Firmware baseline build:
  See docs/automation.md or run the Docker command in README.md.
EOF
