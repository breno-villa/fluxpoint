# Architecture decision records

ADRs capture decisions that are expensive to reverse. Each record states the context, the decision, and the consequences. Superseding a decision means adding a new ADR that references the old one.

| ADR | Decision |
|---|---|
| [0001](0001-project-scope.md) | Project scope and v1 MVP |
| [0002](0002-mcu-firmware-base.md) | Controller and firmware base |
| [0003](0003-connectivity.md) | BLE split, USB host, right-half central |
| [0004](0004-low-profile-power.md) | Low-profile stack, battery, and case |
| [0005](0005-trackpoint.md) | TrackPoint integration |
| [0006](0006-display.md) | Display and power behavior |
| [0007](0007-magnetic-mount.md) | Magnetic mounting system |
| [0008](0008-pcb-strategy.md) | PCB strategy and assembly |
| [0009](0009-security-deferred.md) | Security, fingerprint, FIDO2 deferred |
| [0010](0010-configurator-app.md) | Flutter configurator |
| [0011](0011-automation.md) | Automation and toolchain |
| [0012](0012-licensing.md) | Licensing and repository |

## Template

```markdown
# ADR NNNN: Title

- Status: Proposed | Accepted | Superseded
- Date: YYYY-MM-DD
- Related: links

## Context

What problem or force led to this decision?

## Decision

What was decided?

## Consequences

What becomes easier, harder, or required?
```
