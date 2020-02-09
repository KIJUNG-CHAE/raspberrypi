import RPi.GPIO as IoPort
import time

def KeyHit(channel):
    global SCK
    SCK=True
    if channel==Switch1:
        SCK = True
    elif channel==Switch2:
        SCK = False


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


MOSI = 18
SCK_AorB = 23

Switch1 = 7
Switch2 = 8

SCK = None

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(MOSI,IoPort.OUT)
IoPort.setup(SCK_AorB,IoPort.OUT)
IoPort.setup(Switch1,IoPort.IN)
IoPort.setup(Switch2,IoPort.IN)
IoPort.add_event_detect(Switch1,IoPort.FALLING,callback=KeyHit)
IoPort.add_event_detect(Switch2,IoPort.FALLING,callback=KeyHit)

while True:
    if SCK == None:
        continue
    caseK(SCK,1,0.2)
    caseK(SCK,1,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,1,0.2)
    caseK(SCK,0,0.2)
    caseK(SCK,0,0.2)
    SCK=None