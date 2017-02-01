import pygame.mixer
from pygame.mixer import Sound

pygame.mixer.init()
drum = Sound("samples/drum_tom_mid_hard.wav")
while True:
    drum.play()
