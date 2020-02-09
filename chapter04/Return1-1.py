import RPi.GPIO as IoPort
import time
IoPort.setmode(IoPort.BCM)

def DisplayState(St):
    if St == 1:
        IoPort.output(port1,True)
        IoPort.output(port2,False)
    elif St == 2:
        IoPort.output(port1,False)
        IoPort.output(port2,True)
    elif St == 3:
        IoPort.output(port1,True)
        IoPort.output(port2,True)
    elif St == 4:
        IoPort.output(port1,False)
        IoPort.output(port2,False)
        
def GetKey(key,St):
    if IoPort.input(key) ==True:
        return St
    time.sleep(0.1)
    while True:
        if IoPort.input(key)==True:
            break
    time.sleep(0.1)
    return St+1

Key1=8
Key2=7
port1=18
port2=23
IoPort.setwarnings(False)
IoPort.setup(Key1,IoPort.IN)
IoPort.setup(Key2,IoPort.IN)
IoPort.setup(port1,IoPort.OUT)
IoPort.setup(port2,IoPort.OUT)

State = 1

while True:
    DisplayState(State)
    if State == 1:
        State = GetKey(Key1,State)
    elif State == 2:
        State = GetKey(Key1,State)
        if GetKey(Key2,0)>0:
            break;
    elif State ==3:
        State = GetKey(Key1,State)
    else:
        State = GetKey(Key1,State)
        if GetKey(Key2,0) > 0:
            break;
    if State > 4:
        State = 1
DisplayState(State)

        
