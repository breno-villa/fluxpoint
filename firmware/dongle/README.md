# Dongle (Phase 5)

A future ZMK dongle can become the split central and present a single USB HID device to the host. It is not part of v1.

## Constraints

- The TrackPoint is on the right half; if the dongle becomes central, the TrackPoint must move to the dongle or the driver/split role must change.
- The dongle needs its own enclosure and USB connector.
- The fourth nice!nano clone can be used as a dongle/spare.
- ZMK dongle support is documented; the build target is a central with no keys.

## TODO

- [ ] Decide dongle form factor (USB-A/USB-C)
- [ ] Decide TrackPoint placement/role
- [ ] Build target
- [ ] Case
- [ ] Latency/battery measurement
