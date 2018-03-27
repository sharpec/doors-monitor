from gpiozero import LED
from time import sleep

red = LED(4)

while True:
    red.on()
    sleep(0.2)
    red.off()
    sleep(3)
