# Architecture decision records

ADRs capture decisions that are expensive to reverse. Each record states the context, the decision, and the consequences. Superseding a decision means adding a new ADR that references the old one.

| ADR | Decision | Status | Date |
|---|---|---|---|
| [0001](0001-project-scope.md) | Project scope and v1 MVP | Accepted | 2026-11-05 |
| [0002](0002-mcu-firmware-base.md) | Controller and firmware base | Accepted | 2026-11-05 |
| [0003](0003-connectivity.md) | BLE split, USB host, right-half central | Accepted | 2026-11-05 |
| [0004](0004-low-profile-power.md) | Low-profile stack, battery, and case | Accepted | 2026-11-05 |
| [0005](0005-trackpoint.md) | TrackPoint integration | Accepted | 2026-11-05 |
| [0006](0006-display.md) | Display and power behavior | Accepted | 2026-11-05 |
| [0007](0007-magnetic-mount.md) | Magnetic mounting system | Accepted | 2026-11-05 |
| [0008](0008-pcb-strategy.md) | PCB strategy and assembly | Accepted | 2026-11-05 |
| [0009](0009-security-deferred.md) | Security, fingerprint, FIDO2 deferred | Accepted | 2026-11-05 |
| [0010](0010-configurator-app.md) | Flutter configurator | Accepted | 2026-11-05 |
| [0011](0011-automation.md) | Automation and toolchain | Accepted | 2026-11-05 |
| [0012](0012-licensing.md) | Licensing and repository | Accepted | 2026-11-05 |
| [0013](0013-pin-map.md) | Pin map and board-level interfaces | Proposed | 2026-11-05 |

## Template

```markdown
# ADR NNNN: Title

- **Status:** Proposed | Accepted | Superseded
- **Date:** YYYY-MM-DD
- **Related:** links

## Context

What problem or force led to this decision?

## Decision

What was decided?

## Consequences

What becomes easier, harder, or required?
```
