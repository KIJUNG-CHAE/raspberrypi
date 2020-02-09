import RPi.GPIO as IoPort
import time

Led1 = 18
Led2 = 23

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(Led1,IoPort.OUT)
IoPort.setup(Led2,IoPort.OUT)

def DisplayState(Ld1,Ld2):
    IoPort.output(Led1,Ld1)
    IoPort.output(Led2,Ld2)

def StateWork(st):
    if st == 1:
        return False,False
    elif st == 2:
        return True,False
    elif st == 3:
        return True,True
    else :
        return False,True
    
State = 1

while True:
    Ld1, Ld2 = StateWork(State)
    DisplayState(Ld1,Ld2)
    State += 1
    time.sleep(0.8)
    
    if State >4:
        State = 1


    