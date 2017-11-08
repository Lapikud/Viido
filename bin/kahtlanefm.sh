#!/bin/bash
while true; do
GST_DEBUG=2 gst-launch-1.0 pulsesrc device=alsa_output.pci-0000_00_09.0.analog-stereo.monitor ! audioconvert ! audio/x-raw,channels=2 ! taginject tags="title=Viido,artist=Lapikud" ! vorbisenc quality=0.8 ! oggmux ! shout2send ip=kahtlane.eu port=8000 username= password= mount=live
sleep 10
done
