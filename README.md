# arctis-ctl
Configuration tool for the SteelSeries Arctis headset on Linux.

## Info
Since there is no SteelSeries driver on Linux and I still want to control the LEDs in harmony with e.g. [razer-cli](https://github.com/LoLei/razer-cli/) I have to resort to this.

### Disclaimer
:warning: This is a WIP. Only tested on the Arctis 5. (Literally hardcoded HID ID)  
Possibly in a non-working state at any given time.  
CLI will be exposed once everything is ~working~ stable.  
Different implementation using fork of `sibctrl` and `libusb1` can be found [here](https://github.com/LoLei/sibctrl).
