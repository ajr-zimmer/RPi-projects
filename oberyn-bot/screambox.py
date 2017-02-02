#!/usr/bin/python
from __future__ import division
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
ellaria = Sound("ellaria.wav")
oberyn = Sound("oberyn.wav")
headsplosion = Sound("headsplosion.wav")
ellaria_channel = pygame.mixer.find_channel()
ellaria_channel.set_volume(0)
ellaria_channel.queue(ellaria)
oberyn_channel = pygame.mixer.find_channel()
oberyn_channel.set_volume(0)
oberyn_channel.queue(oberyn)

last_readf1 = 0
last_readf2 = 0

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
    ellaria_channel.queue(ellaria)
    oberyn_channel.queue(oberyn)
    ldr_value = ldr_channel.raw_value
    force1_value = force1_channel.raw_value
    force2_value = force2_channel.raw_value
    
    force1_change = abs(force1_value - last_readf1)
    force2_change = abs(force2_value - last_readf2)
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

