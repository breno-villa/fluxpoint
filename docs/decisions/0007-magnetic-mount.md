# ADR 0007: Magnetic mounting system

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [BOM](../bom.md)

## Context

The keyboard should work flat on a desk, attached to a chair arm, or mounted at an angle on a desk/other surface. The mounts do not need to travel; the keyboard does. A quick-release magnetic interface is desirable, but it must not make the keyboard wobble or interfere with the antenna/TrackPoint.

## Decision

- 4x N52 magnets per half, embedded in the case bottom.
- Matching 1 mm steel plate with a 1/4"-20 threaded boss.
- Camera-style ball head and clamp for angle and attachment.
- Two alignment pins or a shallow recess to prevent rotation.
- Rubber feet for flat desk use; the magnetic plate is an accessory.
- Pull-force target: ≥2x the half's weight.
- Magnet size finalized after a pull-force test; 8x2 or 10x2 mm are candidates.

## Consequences

- The case bottom needs magnet pockets and a flat seating plane around the battery pocket.
- The steel plate/mount is a separate, non-portable accessory.
- Magnet placement is checked against the antenna and TrackPoint; RF range is measured.
- The design is compatible with standard camera mounting hardware.
