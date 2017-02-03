#!/usr/bin/python
from __future__ import division
from gpiozero import MCP3008
import time
import pygame.mixer
from pygame.mixer import Sound

delay = 0.5
# Create GPIO components
ldr_channel = MCP3008(0)
force1_channel = MCP3008(1)
force2_channel = MCP3008(2)

# Initialize sound components
pygame.mixer.init()
ellaria = Sound("ellaria.wav")
oberyn = Sound("oberyn.wav")
headsplosion = Sound("headsplosion.wav")
# Find open channels and set the volume to 0 initially
ellaria_channel = pygame.mixer.find_channel()
ellaria_channel.set_volume(0)
ellaria_channel.queue(ellaria)
oberyn_channel = pygame.mixer.find_channel()
oberyn_channel.set_volume(0)
oberyn_channel.queue(oberyn)
light_channel = pygame.mixer.find_channel()
light_channel.set_volume(0)
light_channel.queue(headsplosion)
# Previous values of sensors to calculate how much the value has changed
last_readl1 = 0
last_readf1 = 0
last_readf2 = 0

# The following three methods convert the analog values to a number
# in the range of 0.0-1.0, in order to set the volume of each channel
def set_crunch_volume(sensor_value):
    set_volume = sensor_value / 9.00
    set_volume = round(set_volume)
    set_volume = int(set_volume)
    set_volume = set_volume / 100
    return set_volume

def set_scream_volume(sensor_value):
    set_volume = sensor_value - 512
    set_volume = set_volume / 5.12
    set_volume = round(set_volume)
    set_volume = int(set_volume)
    set_volume = set_volume / 100
    return 1 - set_volume

def is_change_significant(sensor_change):
    tolerance = 3
    if(sensor_change > tolerance):
        return True
    return False

while True:
    light_channel.queue(headsplosion)
    ellaria_channel.queue(ellaria)
    oberyn_channel.queue(oberyn)

    # Grab analog values from sensors (0-1023)
    ldr_value = ldr_channel.raw_value
    force1_value = force1_channel.raw_value
    force2_value = force2_channel.raw_value
    
    ldr_change = abs(ldr_value - last_readl1)
    force1_change = abs(force1_value - last_readf1)
    force2_change = abs(force2_value - last_readf2)

    if(is_change_significant(ldr_change)):
        light_channel.set_volume(set_crunch_volume(ldr_value))
        last_readl1 = ldr_value

    if(is_change_significant(force1_change)):
        ellaria_channel.set_volume(set_scream_volume(force1_value))
        last_readf1 = force1_value

    if(is_change_significant(force2_change)):
        oberyn_channel.set_volume(set_scream_volume(force2_value))
        last_readf2 = force2_value

    print "---------------------------------------"
    print("ldr value: %d" % ldr_value)
    print("force 1 value: %d" % force1_value)
    print("force 2 value: %d" % force2_value)
    time.sleep(delay)

