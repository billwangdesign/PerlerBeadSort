
from adafruit_servokit import ServoKit


#kit = ServoKit(channels=16, address=65)
#kit.servo[0].angle = 0


class MachineServo(ServoKit):
    def __init__(self, address=64, channel=0, min=0, max=90, leftPos=30, rightPos=60, pos=0):
        self._channel = channel
        self._min = min
        self._max = max
        self._leftPos = leftPos
        self._rightPos = rightPos
        self._pos = pos

    def left(self):
        self._pos = self._leftPos
        self.servo[self._channel].angle = self._leftPos
    
    def right(self):
        self._pos = self._rightPos
        self.servo[self._channel].angle = self._rightPos
    def command(self, c):
        if c == True:
            self.left()
        else:
            self.right()

    def setpos(self):
        return self._pos

    def stat(self):
        print("Channel = ", self._channel)
        print("min = ", self._min)
        print("max = ", self._max)
        print("lefPos = ", self._leftPos)
        print("rightPos = ", self._rightPos)
        print("pos = ", self._pos)


#kit2 = MachineServo(address=65)
#kit2.servo[0].angle = 60