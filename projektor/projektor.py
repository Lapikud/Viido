#!/usr/bin/env python3
import serial
from time import sleep

def on_hdmi():
    p = Projektor("/dev/ttyS0")
    print("HDMI ON")
    while True:
        if p.get_power() != "ON":
            print("PROJECTOR ON")
            p.on()

        elif p.get_source() != "HDMI":
            print("SWITCHING HDMI")
            p.hdmi()
            break
        
        else:
            break
        sleep(1)
    print("DONE")
    p.close()

def on_vga():
    p = Projektor("/dev/ttyS0")
    print("VGA ON")
    while True:
        if p.get_power() != "ON":
            print("PROJECTOR ON")
            p.on()

        elif p.get_source() != "VGA":
            print("SWITCHING VGA")
            p.vga()
            break

        else:
            break
        sleep(1)
    print("DONE")
    p.close()


def get_status():
    p = Projektor("/dev/ttyS0")
    if p.get_power() == "OFF":
        status = "off"

    else:
        status = p.get_source()
    print("DONE")
    p.close()
    return status

def off():
    p = Projektor("/dev/ttyS0")
    p.off()

class Projektor:
    def __init__(self, device):
        self.ser = serial.Serial(device, 115200, timeout=1)

    def close(self):
        self.ser.close()

    def ___delete__(self, instance):
        self.close()

    def on(self):
        self.ser.write(b"\r*pow=on#\r")

    def off(self):
        self.ser.write(b"\r*pow=off#\r")

    def hdmi(self):
        self.ser.write(b"\r*sour=hdmi#\r")

    def vga(self):
        self.ser.write(b"\r*sour=RGB2#\r")

    def get_source(self):
        self.ser.read()
        self.ser.write(b"\r*sour=?#\r")

        while True:
            c = self.ser.read(1)
            if c == b">":
                self.ser.read(17)
                source = self.ser.read(4)
                if source == b"HDMI":
                    return "hdmi"
                elif source == b"RGB2":
                    return "vga"
            elif not c:
                break

    def get_power(self):
        self.ser.read()
        self.ser.write(b"\r*pow=?#\r")

        while True:
            c = self.ser.read(1)
            if c == b">":
                self.ser.read(15)
                status = self.ser.read(3)

                if status == b"k i":
                    return None
                elif status == b"ON#":
                    return "ON"
                elif status == b"OFF":
                    return "OFF"

            elif not c:
                break


if __name__ == "__main__":

    p = Projektor("/dev/ttyS0")
    while True:
        if p.get_power() != "ON":
            print("POWER ON")
            p.on()

        elif p.get_source() != "HDMI":
            print("switching HDMI")
            p.hdmi()
        else:
            break
