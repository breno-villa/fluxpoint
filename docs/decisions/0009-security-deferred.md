# ADR 0009: Security, fingerprint, and FIDO2 deferred

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Feasibility](../feasibility.md), [Architecture](../architecture.md)

## Context

The original vision included a FIDO2/CTAP2 security key and a fingerprint reader. Implementing FIDO2 on the keyboard controller is not a small feature: the nRF52840 is not a secure element, credential storage/PIN/attestation need care, and fingerprint as user verification requires a match-in-sensor module and a custom bridge. The HLK-ZW0905 is UART/3.3 V with 50 templates and 200 mA peaks; it has no ready ZMK/FIDO2 integration.

## Decision

- FIDO2/CTAP2 and fingerprint are out of scope for v1.
- The right PCB reserves a 4-pin UART header and load switch for the fingerprint module, unpopulated.
- A future FIDO2 design must use a separate security architecture: a dedicated security MCU running OpenSK-like firmware, a certified external key, or a secure element. The keyboard MCU alone is not the security boundary.
- A future fingerprint design must define user presence vs user verification, anti-spoof, enrollment, privacy, and fallback.

## Consequences

- v1 stays focused on the keyboard and pointing device.
- The expansion header keeps a hardware path open without committing to a security architecture.
- FIDO2/fingerprint will require a separate ADR, threat model, and likely a new board/revision.
- The keyboard can still use an external security key in the meantime.
