import RPi.GPIO as IoPort
import time
def keyInput(key):
    if IoPort.input(key)==True:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key)==True:
            break
    time.sleep(0.1)
    return True

def sigA(port1,port2,delay):
    IoPort.output(port1,False)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port2,False)
    time.sleep(delay)

def sigB(port1,port2,delay):
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port2,False)
    time.sleep(delay)
    
def sigC(port1,port2,delay):
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
    
delay = 0.2
port1 = 18
port2 = 23
key7 = 7
key8 = 8

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(port1,IoPort.OUT)
IoPort.setup(port2,IoPort.OUT)
IoPort.setup(key7,IoPort.IN)
IoPort.setup(key8,IoPort.IN)
# main

while True:
    if keyInput(key7):
        delay = 0.2
    elif keyInput(key8):
        delay = 0.4
    else:
        continue
    sigA(port1,port2,delay)
    sigA(port1,port2,delay)
    sigA(port1,port2,delay)
    sigS(port1,port2,delay)
    sigO(port1,port2,delay)
    sigS(port1,port2,delay)
    sigA(port1,port2,delay)
    sigA(port1,port2,delay)
    