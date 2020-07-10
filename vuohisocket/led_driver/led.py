# -*- coding: utf-8 -*-

import serial
import os
import argparse


class LedStripSerialException(Exception):
    pass

class LedStripSerial:

    def __init__(self, address):
        os.system("stty -F {} -hupcl".format(address))
        self.serial = serial.Serial(address, 9600, timeout=2)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.serial.close()

    def write_to_ser(self, *rgb):
        color_names = ('red', 'green', 'blue')
        i = 0

        if not len(rgb) == 3:
            raise LedStripSerialException("Check arguments! 3 needed for rgb, {} arguments given".format(len(rgb)))

        for v in rgb:
            if not 0 <= v <= 255:
                raise LedStripSerialException("Check rgb values (0 - 255) Argument for {} is {}".format(
                    color_names[i],
                    v)
                )
            i += 1
        output = str(rgb[0]) + ',' + str(rgb[1]) + ',' + str(rgb[2]) + '\n'
        try:
            self.serial.write(output.encode())
        except serial.serialutil.SerialTimeoutException as e:
            self.serial.close()
            raise LedStripSerialException(str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to set the rgb led strip colors under my f***ing table.')
    parser.add_argument("-r", "--red", help="Red value for solidCustom program", type=int, metavar="[0-255]")
    parser.add_argument("-g", "--green", help="Green value for solidCustom program", type=int, metavar="[0-255]")
    parser.add_argument("-b", "--blue", help="Blue value for solidCustom program", type=int, metavar="[0-255]")
    args = parser.parse_args()
    with LedStripSerial('/dev/ttyACM0') as led_strip:
        print("r: {} g: {} b: {}".format(args.red, args.green, args.blue))
        led_strip.write_to_ser(args.red, args.green, args.blue)

