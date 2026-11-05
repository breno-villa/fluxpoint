# ADR 0012: Licensing and repository

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [README](../../README.md), [NOTICE](../../NOTICE)

## Context

The project is inspired by the Corne keyboard (foostan/crkbd), whose repository provides MIT and CC BY 4.0 terms. The builder wants a public, open project with clear hardware, firmware, and documentation licensing. The project name is Fluxpoint; the local working directory may remain `corne-hybrid` until the repository is renamed.

## Decision

- Public repository (GitHub, `fluxpoint`).
- Hardware: CERN-OHL-S-2.0.
- Firmware: MIT.
- Documentation: CC BY 4.0.
- Preserve Corne attribution and license notices in `NOTICE`.
- Use the name `Fluxpoint` in documentation, repository, and case branding.
- Do not relicense Corne-derived files; keep their original notices and mark modifications.

## Consequences

- The project is open hardware and open source.
- CERN-OHL-S-2.0 is strongly reciprocal for hardware; derivative hardware must comply.
- Corne-derived blocks must retain MIT/CC BY 4.0 attribution.
- The repository must include the full license texts and a NOTICE file.
