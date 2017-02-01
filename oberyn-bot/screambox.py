#!/usr/bin/python
 
from gpiozero import MCP3008
import time
import pygame.mixer
from pygame.mixer import Sound

#Define variables
delay = 0.5
ldr_channel = MCP3008(0)
force1_channel = MCP3008(1)
force2_channel = MCP3008(2)
pygame.mixer.init()
scream = Sound("ellaria-sand-scream.wav")

#Readings on Light Sensor
last_read = 0
tolerance = 5

while True:
    ldr_changed = False
    
    scream.play()
    ldr_value = ldr_channel.raw_value
    force1_value = force1_channel.raw_value
    force2_value = force2_channel.raw_value
    
    ldr_change = abs(ldr_value - last_read)
    if(ldr_change > tolerance):
        ldr_changed = True
    if(ldr_changed):
        set_volume = ldr_value / 10.24
        set_volume = round(set_volume)
        set_volume = int(set_volume)
        set_volume = set_volume / 100
        scream.set_volume(set_volume)
        last_read = ldr_value

    print "---------------------------------------"
    print("ldr value: %d" % ldr_value)
    print("force 1 value: %d" % force1_value)
    print("force 2 value: %d" % force2_value)
    time.sleep(delay)

