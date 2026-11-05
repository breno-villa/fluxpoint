# ADR 0006: Display and power behavior

- **Status:** Accepted
- **Date:** 2026-11-05
- **Related:** [Architecture](../architecture.md), [Requirements](../requirements.md)

## Context

The builder has a 0.91" 128x32 SSD1306 I2C OLED. It is easy to use but draws 15–25 mA when on and can suffer burn-in. nice!view uses a Sharp memory LCD (~10 µA) but costs more and uses SPI. The OLED should be off by default and used only for status checks.

## Decision

- v1 uses the SSD1306 OLED on the right half.
- The OLED is off by default.
- A key combination wakes it for 10 seconds; a custom ZMK behavior handles the timer.
- Blanking is software-based first; a load-switch footprint is reserved if the sleep current is too high.
- The final PCB includes a nice!view-compatible footprint/adapter path; the OLED and nice!view share a 3-GPIO display header and are alternatives, not both populated.
- Status content: battery, output, layer, and connection; security state is added only if a future security feature exists.

## Consequences

- v1 validates the display with the part on hand.
- Battery life depends on the OLED remaining off; the 10-second behavior is part of acceptance.
- The final PCB supports a low-power display upgrade without a board respin; the shared display header must keep the I2C and SPI pin functions compatible.
- The display behavior must be tested with ZMK Studio and split roles.
