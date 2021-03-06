"""
Based on:
https://github.com/andrepl/rivalctl/
"""

import pyudev
import hidrawpure as hidraw

HS_HID_ID = "0003:00001038:000012AA"  # 1038:12aa SteelSeries ApS SteelSeries Arctis 5
# HS_HID_ID = "0003:00001532:00000060"  # 1532:0060 Razer USA, Ltd Razer Lancehead Tournament Edition
# HS_HID_ID = "0003:00001532:0000021a"  # 1532:021a Razer USA, Ltd BlackWidow X Tournament Edition Chroma


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
    print("Found device: ")
    print(device.getName())
    print(device.getInfo())
    print(device.getPhysicalAddress())
    # print(device.getRawReportDescriptor())

    print("Sending report...")
    device.sendFeatureReport(report)


def create_report():
    # Hardcoded test report
    color = [123, 0, 55]
    args = (chr(1),) + tuple([chr(b) for b in color])
    # print(args)
    # report = "\x08%s%s%s%s" % args
    # report = '\x09'  # Save

    report_full = "\x1c\x00\xa0\x09\x4d\x4d\x03\x9f\xff\xff\x00\x00\x00\x00\x1b\x00\x00\x01\x00\x04\x00\x00\x02\x25\x00\x00\x00\x01\x06\x81\x43\x01\x22\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    report_leftover = "\x06\x81\x43\x01\x22\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    report = report_leftover
    print("Report length: {}".format(len(report)))
    print(report)

    return report


def main():
    print("> arctis_ctl: ")
    report = create_report()
    send(report)


if __name__ == "__main__":
    """ This is executed when run from the command line - obsolete """
    main()
