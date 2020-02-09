import RPi.GPIO as IoPort
import time

MOSI = 18
SCK_AorB = 23

Switch1 = 7
Switch2 = 8

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(MOSI,IoPort.OUT)
IoPort.setup(SCK_AorB,IoPort.OUT)
IoPort.setup(Switch1,IoPort.IN)
IoPort.setup(Switch2,IoPort.IN)

def KeyInput(Key): #switch input -> use while
    if IoPort.input(Key) == True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(Key) == True:
            break
    time.sleep(0.1)
    return True

def case(SCK, TF, delay):
    IoPort.output(MOSI,TF)
    IoPort.output(SCK_AorB,SCK)
    time.sleep(delay)

def caseK(SCK,TF, delay):
    ReverseSCK = False
    if SCK==False:
        ReverseSCK = True
    case(SCK, TF, delay)
    case(ReverseSCK, TF, 2*delay)
    case(SCK, TF, delay)

SCK = True
while True:
    if KeyInput(Switch1)==True:
        SCK = True
    elif KeyInput(Switch2)==True:
        SCK = False
    
    caseK(SCK,1,0.2)
    caseK(SCK,1,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,1,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,0,0.2)