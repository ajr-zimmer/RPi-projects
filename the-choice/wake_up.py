import os
import sys
from gpiozero import LED, Button
from signal import pause

#Initialize Raspberry Pi component
launch_button = Button(2)

print "Wake up..."
print "Press the button, please."

def startServer():
    os.system("python server.py")

launch_button.when_pressed = startServer

pause()
