from gpiozero import LED, Button
from signal import pause

redLED = LED(22)
blueLED = LED(17)
button = Button(2)

def reality():
    redLED.on()
    blueLED.off()

def bliss():
    redLED.off()
    blueLED.on()

button.when_pressed = reality
button.when_released = bliss

pause()
