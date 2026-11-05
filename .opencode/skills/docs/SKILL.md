---
name: docs
description: Use when updating Fluxpoint requirements, architecture, roadmap, feasibility, ADRs, documentation links, or project conventions.
---

# Documentation workflow

Read `docs/README.md` first. Documentation is English; code identifiers are English.

## Where things go

- `docs/requirements.md` — scope, functional/non-functional requirements, acceptance criteria.
- `docs/architecture.md` — system blocks, connectivity, power, firmware, mechanical stack, pin budget.
- `docs/roadmap.md` — phases, milestones, risks, decision gates.
- `docs/feasibility.md` — proven vs feasible vs research.
- `docs/bom.md` — inventory, missing parts, suppliers.
- `docs/bringup.md` — bench procedures and acceptance tests.
- `docs/automation.md` — toolchain, MCPs, skills, CI, scripts.
- `docs/trackpoint.md` — TrackPoint measurements/protocol/reset.
- `docs/layout.md` — physical layout, layers, pointing bindings.
- `docs/decisions/` — ADRs.

## Rules

- A decision that changes scope, architecture, interfaces, or safety gets an ADR.
- ADR format: context, decision, consequences; status/date/related links.
- Update cross-links when moving/renaming files.
- Keep measurements in mm and state confidence.
- Do not silently resolve open questions; record them.
- Do not add generated artifacts or binary files to docs.

## Checks

```bash
python tools/fluxpoint_cli.py check-docs
python tools/fluxpoint_cli.py check-config
```

Fix broken links before committing. CI runs both checks.

## Tone

- Direct, specific, engineering-focused.
- Separate requirements ("must") from current implementation and open risks.
- Prefer tables/checklists over prose where it improves scanning.
