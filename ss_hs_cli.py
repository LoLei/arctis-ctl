# https://github.com/andrepl/rivalctl/

import pyudev
import hidrawpure as hidraw

HS_HID_ID = "0003:00001038:000012AA"


def find_device_path():
    context = pyudev.Context()
    for dev in context.list_devices(HID_ID=HS_HID_ID):
        if dev.sequence_number == 0:
            children = list(dev.children)
            if children:
                child = children[0]
                if child.subsystem == 'hidraw':
                    print(child.properties.device.sys_name)
                    return child['DEVNAME']


def open_device(dev_path=None):
    if dev_path is None:
        dev_path = find_device_path()
    return hidraw.HIDRaw(open(dev_path, 'w+'))


def send(report, device=None):
    """send a report packet to the device"""
    if device is None:
        device = open_device()
    device.sendFeatureReport(report)


def main():
    ##### Hardcoded test report
    color = [123, 0, 55]
    args = (chr(1),) + tuple([chr(b) for b in color])
    print(args)
    # report = "\x08%s%s%s%s" % args
    b1 = "\x87"
    b2 = "\x22"

    report = "\x04" + "\x40" + "\x01" + "\x11" + b1 + b2 + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00" + "\x00"

    # report[4] = b1
    # report[5] = b2

    print(report)
    ######

    send(report)


if __name__ == "__main__":
    """ This is executed when run from the command line - obsolete """
    main()
