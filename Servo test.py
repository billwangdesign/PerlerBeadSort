#!/usr/bin/python
import sys

sys.path.append("C:\Python36\Lib\site-packages")
import gpiozero
from time import sleep

servo = Servo(17)

while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)