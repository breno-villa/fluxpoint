# ADR 0008: PCB strategy and assembly

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [BOM](../bom.md), [Roadmap](../roadmap.md)

## Context

The Corne 3x6+3 matrix and nice!nano footprint are proven. The project needs a TrackPoint, OLED, battery, magnets, and a future fingerprint header, none of which fit a stock Corne PCB. Two mirrored boards make per-side features and debugging easier than a reversible board.

## Decision

- Design custom PCBs, reusing the proven Corne matrix/controller blocks as reference.
- Two mirrored PCBs (left and right), 1.6 mm, 2 layers, JLCPCB fabrication.
- Right PCB carries the TrackPoint connector, OLED, and future fingerprint header/load switch.
- Left PCB is simpler; it still has the matrix, controller, battery, and power switch.
- Mixed connectors: JST-PH for battery, FPC/FFC or solder pads for OLED/TrackPoint, 2.54 mm socket for the controller.
- Hand assembly; the only fine-pitch parts are the optional FPC connectors, which can be pre-assembled, ordered assembled, or replaced by solder pads/headers.
- Preserve Corne attribution and license notices.

## Consequences

- More layout work than a reversible board, but clearer per-side features and easier review.
- Two fabrication designs can share a panel/order.
- The TrackPoint FPC and OLED connectors must be selected after the module test.
- The expansion header is unpopulated in v1 but preserves the fingerprint option.
