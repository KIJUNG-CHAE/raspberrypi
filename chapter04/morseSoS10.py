import RPi.GPIO as IoPort
import time


def keyHit(key):
    global work
    if key == key7:
        work = True
    elif key == key8:
        work = False
        IoPort.output(port1,False)
        IoPort.output(port2,False)

def sigA(port1,port2,delay):
    if work == False:
        return 
    IoPort.output(port1,False)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port2,False)
    time.sleep(delay)

def sigB(port1,port2,delay):
    if work == False:
        return 
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port2,False)
    time.sleep(delay)
    
def sigC(port1,port2,delay):
    if work == False:
        return 
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port1,False)
    IoPort.output(port2,False)
    time.sleep(delay)
    
def sigS(port1,port2,delay):
    sigC(port1,port2,delay)
    sigC(port1,port2,delay)
    sigC(port1,port2,delay)
    sigA(port1,port2,delay)
    
def sigO(port1,port2,delay):
    sigB(port1,port2,delay)
    sigC(port1,port2,delay)
    sigB(port1,port2,delay)
    sigC(port1,port2,delay)
    sigB(port1,port2,delay)
    sigC(port1,port2,delay)
    sigA(port1,port2,delay)
    
delay = 0.4
port1 = 18
port2 = 23
key7 = 7
key8 = 8
work = False

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(port1,IoPort.OUT)
IoPort.setup(port2,IoPort.OUT)
IoPort.setup(key7,IoPort.IN)
IoPort.setup(key8,IoPort.IN)
IoPort.add_event_detect(key7,IoPort.FALLING,callback=keyHit)
IoPort.add_event_detect(key8,IoPort.FALLING,callback=keyHit)

# main

while True:
    if work == False:
        continue
    sigA(port1,port2,delay)
    sigA(port1,port2,delay)
    sigA(port1,port2,delay)
    sigS(port1,port2,delay)
    sigO(port1,port2,delay)
    sigS(port1,port2,delay)
    sigA(port1,port2,delay)
    sigA(port1,port2,delay)
    
    