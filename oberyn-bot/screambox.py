#!/usr/bin/python
 
from gpiozero import mcp3008
import time
from pygame.mixer import Sound

#Define variables
delay = 0.5
ldr_channel = mcp3008(0)
force1_channel = mcp3008(1)
force2_channel = mcp3008(2)
pygame.mixer.init()
scream = Sound("scream1.wav")

while true:
    scream.play()
    ldr_value = ldr_channel.raw_value
    force1_value = force1_channel.raw_value
    force2_value = force2_channel.raw_value
    print "---------------------------------------"
    print("ldr value: %d" % ldr_value)
    print("force 1 value: %d" % force1_value)
    print("force 2 value: %d" % force2_value)
    time.sleep(delay)

