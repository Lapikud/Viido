#!/usr/bin/env python3
from bottle import get, post, request, run
import projektor

@get("/status")
def status():
    print("asking status")
    return projektor.get_status()

@post("/status")
def set_status():
    mode = request.forms.get("mode")
    print("SETTING STATUS TO", mode)
    if mode == "off":
        projektor.off()
    elif mode == "hdmi":
        projektor.on_hdmi()
    elif mode == "vga":
        projektor.on_vga()


    return "OK"



if __name__ == "__main__":
    run(host="127.0.0.1", port=6999, debug=False)
