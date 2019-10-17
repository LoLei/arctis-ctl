# https://hackaday.com/2011/03/17/writing-python-drivers-for-input-devices/
import sys

pipe = open('/dev/input/by-id/usb-SteelSeries_SteelSeries_Arctis_5_00000000-event-if05', 'r')
action = []
spacing = 0
while 1:
    for character in pipe.read(1):
        action += [character]
        if len(action) == 8:
            for byte in action:
                sys.stdout.write('%02X ' % byte)
            spacing += 1
            if spacing == 1:
                sys.stdout.write('\n')
                spacing = 0
            sys.stdout.write('\n')
            sys.stdout.flush()
            action = []
