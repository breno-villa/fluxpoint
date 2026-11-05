# PCB

Planned Phase 2 deliverables: two mirrored KiCad boards for the left and right halves.

## Right half

- nice!nano clone socket, matrix, battery connector, power switch.
- TrackPoint 4-pin FPC connector (0.5 mm) near the right thumb cluster.
- Shared 3-GPIO display header: I2C OLED (v1) or SPI nice!view (alternative); only one populated.
- Future fingerprint 4-pin UART header + load switch (unpopulated).
- Antenna keepout.

## Left half

- Same matrix/controller/power blocks.
- No TrackPoint, fingerprint header, or display in v1.

## Stack and fabrication

- 2 layers, 1.6 mm, HASL, 1 oz copper; ENIG optional.
- Choc V1 hot-swap sockets; 1N4148W SOD-123 diodes.
- 2.54 mm controller sockets.
- JST-PH battery connector.
- FR4 switch plate, 1.2–1.6 mm.
- Hand assembly.

## Before layout

- [ ] Close the pin map (matrix, TrackPoint, OLED, battery ADC, expansion).
- [ ] Confirm TrackPoint protocol/reset and connector contact side.
- [ ] Confirm nice!nano clone pinout and 3.3 V current budget.
- [ ] Confirm antenna keepout with battery/magnets.
- [ ] Choose exact FPC/OLED connectors.

## TODO

- [ ] Schematic
- [ ] ERC
- [ ] Layout
- [ ] DRC
- [ ] Gerbers/BOM/pick-and-place
- [ ] Bring-up
