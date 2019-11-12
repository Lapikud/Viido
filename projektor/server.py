#!/usr/bin/env python3
from bottle import get, post, request, run
import serial
import termios

def send(cmd):
    ser = serial.Serial()
    ser.rts = False
    ser.dtr = False
    ser.port = "/dev/ttyS0"
    ser.open()
    ser.write(cmd)
    ser.close()

def send1(cmd):
    port="/dev/ttyUSB0"
    ser = serial.Serial()
    ser.rts = False
    ser.dtr = False
    ser.port = port
    ser.open()
    ser.write(cmd)
    ser.close()


@get("/status")
def status():
    print("asking status")
    return "hdmi"


@post("/status")
def set_status():
    mode = request.forms.get("mode")
    print("SETTING STATUS TO", mode)
    if mode == "off":
        send(b"\r*pow=off#\r")
    elif mode == "on":
        send(b"\r*pow=on#\r")
    elif mode == "viido":
        send1(b"t")
    elif mode == "hdmi":
        send1(b"m")
    elif mode == "steam":
        send1(b"l")
    elif mode == "aux":
        send1(b"a")
    elif mode == "volumeup":
        send1(b"q")
    elif mode == "volumedown":
        send1(b"w")
    


    return "OK"



if __name__ == "__main__":
    run(host="127.0.0.1", port=6999, debug=False)
