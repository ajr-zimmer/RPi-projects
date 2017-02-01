#!/usr/bin/python
 
from gpiozero import MCP3008
import time

#Define Variables
delay = 0.5
ldr_channel = MCP3008(0)
force1_channel = MCP3008(1)
force2_channel = MCP3008(2)
 
while True:
    ldr_value = ldr_channel.raw_value
    force1_value = force1_channel.raw_value
    force2_value = force2_channel.raw_value
    print "---------------------------------------"
    print("LDR Value: %d" % ldr_value)
    print("Force 1 Value: %d" % force1_value)
    print("Force 2 Value: %d" % force2_value)
    time.sleep(delay)
