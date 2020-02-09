import RPi.GPIO as IoPort
import time

def KeyInput(key):
    if IoPort.input(key)==True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key)==True:
            break
    time.sleep(0.1)
    return True

def candle(Port,on,off):
    global Count
    for i in range(0,Count):
        IoPort.output(Port,True)
        time.sleep(on)
        IoPort.output(Port,False)
        time.sleep(off)
        if KeyInput(key1)==True:
            return False
    return True

def State1(Led,sub):
    while True:
        sub -= 0.03/40
        if sub<0:
            sub = 0
        if candle(Led,sub,0.03-sub)==False:
            return sub
        
def State2(Led,sub):
    while True:
        sub += 0.03/40
        if sub>0.03:
            sub = 0.03
        if candle(Led,sub,0.03-sub)==False:
            return sub
        
sub = 0.03
Led = 18
key1= 8
Count = 20

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(Led, IoPort.OUT)
IoPort.setup(key1, IoPort.IN)
while True:
    sub = State1(Led,sub)
    sub = State2(Led,sub)