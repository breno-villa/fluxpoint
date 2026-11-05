# ADR 0011: Automation and toolchain

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Automation](../automation.md), [Roadmap](../roadmap.md)

## Context

The project has many repetitive engineering tasks: docs/links, BOM, KiCad checks, CAD exports, firmware builds, bench logs, and releases. The builder wants agents to automate as much as possible. The machine is Arch Linux with Docker, uv, Node, Rust, and GitHub CLI. KiCad/FreeCAD/OpenSCAD are available as Arch packages.

## Decision

- Install KiCad, FreeCAD, OpenSCAD, ARM GCC, probe-rs, OpenOCD, and sigrok-cli as system packages.
- Use Konnect as the primary KiCad MCP (with the KiCAD-MCP-Server fallback); FreeCAD MCP and OpenSCAD MCP for CAD.
- Use GitHub Actions for documentation/config checks and the baseline ZMK firmware build.
- Use a local automation CLI for docs/config checks, flashing, serial logs, logic capture, and power measurements.
- Create project skills for Fluxpoint, KiCad, ZMK, CAD, bring-up, BOM, and docs.
- Require human review for schematics, PCBs, safety, and releases.

## Consequences

- Faster iteration and fewer manual mistakes.
- Tool versions and MCP compatibility are maintenance risks; pin versions where possible.
- Konnect's move to Konnect-EDA and its commercial licensing must be monitored; the MIT KiCAD-MCP-Server remains a fallback.
- CI cannot replace bench validation; RF, battery safety, and mechanical fit remain manual tests.
