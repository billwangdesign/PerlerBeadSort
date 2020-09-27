from gpiozero import LED
from time import sleep
import pigpio
pigpio.INPUT

pin = PiGPIOPin(17, host='192.168.50.100')

red = LED(pin)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)