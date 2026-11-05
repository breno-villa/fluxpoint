# Fluxpoint documentation

This directory is the source of truth for product requirements, architecture, decisions, and validation.

| Document | Purpose |
|---|---|
| [Requirements](requirements.md) | Scope, functional and non-functional requirements, acceptance criteria |
| [Architecture](architecture.md) | System blocks, connectivity, power, firmware, and mechanical stack |
| [Roadmap](roadmap.md) | Phases, milestones, dependencies, and risks |
| [Feasibility](feasibility.md) | What is proven, what is feasible, and what is research |
| [BOM and inventory](bom.md) | Owned parts, missing parts, estimates, suppliers, tools |
| [Bring-up and acceptance](bringup.md) | Bench procedures and measurable acceptance tests |
| [Automation](automation.md) | Toolchain, MCP servers, skills, CI, and scripts |
| [TrackPoint](trackpoint.md) | Salvaged module data, connector, reset strategy, and test plan |
| [Pin map](pinmap.md) | Candidate matrix, TrackPoint, display, and expansion pins; Phase 1 gate |
| [Bench log](bench-log.md) | Phase 1 measurements, evidence, and exit checklist |
| [Layout and keymap](layout.md) | 42-key layout, layers, thumb cluster, and pointing-device bindings |
| [ADRs](decisions/README.md) | Accepted architecture decisions and trade-offs |

## Conventions

- Documentation is written in English. Code identifiers and commit messages are in English.
- Decisions that change architecture, scope, or interfaces get an ADR in `docs/decisions/`.
- Measurements include units and a confidence note when they come from a caliper or a photo.
- Fabrication outputs (Gerbers, STL, UF2) are generated artifacts and are not committed unless a release explicitly includes them.
- Link checks run in CI: `python tools/fluxpoint_cli.py check-docs`.

## Status

Phase 1. Requirements and architecture are agreed at the product level; the Phase 1 bench shield, pin-map draft, and measurement log exist, but the PCB, case, and final firmware are not designed yet. The baseline Corne configuration and the Phase 1 `fluxpoint_bench` shield validate tooling and breadboard bring-up.
