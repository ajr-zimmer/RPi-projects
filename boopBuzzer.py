from gpiozero import Buzzer
from time import sleep

bz = Buzzer(17)

while True:
  bz.on()
  sleep(1)
  bz.off()
  sleep(1)

