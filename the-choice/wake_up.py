import os
import sys
from gpiozero import LED, Button
from signal import pause

button = Button(2)

print "Wake up..."
print "Press the button, please."

def startServer():
    os.system("python server.py")

button.when_pressed = startServer

pause()
