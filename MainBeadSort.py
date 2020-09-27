from beads import beads
from machine import *
from machineOps import *

def main(): 
    red = beads()
    red.r(44)
    red.g(55)
    red.b(70)
    red.trans(True)
    red.mixed(True)
    red.glow(True)
    red.qty(99)
    #red.stat()
    
    s1 = MachineServo(address = 64, channel=0)
    s2 = MachineServo(address = 64, channel=1)
    s3 = MachineServo(address = 64, channel=2)
    #spare channel 3-7
    
    s4 = MachineServo(address = 64, channel = 8)
    s4b = MachineServo(address = 64, channel = 9)
    s4c = MachineServo(address = 64, channel = 10)
    s4d = MachineServo(address = 64, channel = 11)

    s4e = MachineServo(address = 64, channel = 12)    
    s4f = MachineServo(address = 64, channel = 13)
    s4g = MachineServo(address = 64, channel = 14)
    s4h = MachineServo(address = 64, channel = 15)

    s5 = MachineServo(address = 65, channel = 0)
    s5b = MachineServo(address = 65, channel = 1)
    s5c = MachineServo(address = 65, channel = 2)
    s5d = MachineServo(address = 65, channel = 3)

    s5e = MachineServo(address = 65, channel = 4)
    s5f = MachineServo(address = 65, channel = 5)
    s5g = MachineServo(address = 65, channel = 6)
    s5h = MachineServo(address = 65, channel = 7)

    s6 = MachineServo(address = 65, channel = 8)
    s6b = MachineServo(address = 65, channel = 9)
    s6c = MachineServo(address = 65, channel = 10)
    s6d = MachineServo(address = 65, channel = 11)

    s6e = MachineServo(address = 65, channel = 12)
    s6f = MachineServo(address = 65, channel = 13)
    s6g = MachineServo(address = 65, channel = 14)
    s6h = MachineServo(address = 65, channel = 15)
    

    groupServo = [[s4, s4b, s4c, s4d, s4e, s4f, s4g, s4h], 
    [s5, s5b, s5c, s5d, s5e, s5f, s5g, s5h],
    [s6, s6b, s6c, s6d, s6e, s6f, s6g, s6h]]
    
  

    allmotors = [s1, s2, s3, s4, s5, s6]
    motorsCommand = sort()
    print("from main", motorsCommand)

    # go through motor S1 thru S6 to set left or right position 
    # based on motorCommand boolean
    for i in range(0, 6):
        allmotors[i].command(strtobool(motorsCommand[i]))
        print("S", i+1, " set to: ", allmotors[i].setpos())

    # 2 dimentional array, loop through
    # sxb/c/d/e/f/g/h copy sx servo command
    for k in range(0, 3):
        for j in range(0, 8):

            #if servo being copied current position is left, then set all others in group to left        
            if groupServo[k][0].setpos() == groupServo[k][0]._leftPos:
                groupServo[k][j].left()
            else:
                groupServo[k][j].right()
            #print("row: ", k, "number: ", j, "motor0: ", groupServo[k][0].setpos())
            print("row: ", k, "number: ", j, "motor channel: ", groupServo[k][j]._channel, "motor command " ,groupServo[k][j].setpos())

#64 colors into binary 
#32 16 8 4 2 1
#0  0  0 1 0 1
#color 5 example
#servo 1 2 3 4 5 6
#servo 0 0 0 1 0 1
#servo left left left right left right

#False = right = 0 = 34
#True = left = 1 = 12

def strtobool(k):
    #print("str to bool: ", k)
    if k == '0':
        #print("return false")
        return False
    else:
        #print("return true")
        return True

def sort():
    command = str(format(5, '06b')) #convert number to 6 digit binary
    return command
    
if __name__ == '__main__': main()
