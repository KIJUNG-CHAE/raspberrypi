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

def pulse_a(port1,port2,delay):
    IoPort.output(port1,False)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port2,False)
    time.sleep(delay)

def pulse_b(port1,port2,delay):
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port2,False)
    time.sleep(delay)
    
def pulse_c(port1,port2,delay):
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay)
    IoPort.output(port1,False)
    IoPort.output(port2,False)
    time.sleep(delay)
    
def pulse_A(port1,port2,delay):
    IoPort.output(port1,False)
    IoPort.output(port2,True)
    time.sleep(delay/2)
    IoPort.output(port2,False)
    time.sleep(delay/2)
    IoPort.output(port2,True)
    time.sleep(delay/2)
    IoPort.output(port2,False)
    time.sleep(delay/2)
    
def pulse_B(port1,port2,delay):
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay/2)
    IoPort.output(port2,False)
    time.sleep(delay/2)
    IoPort.output(port2,True)
    time.sleep(delay/2)
    IoPort.output(port2,False)
    time.sleep(delay/2)
    
def pulse_C(port1,port2,delay):
    IoPort.output(port1,True)
    IoPort.output(port2,True)
    time.sleep(delay/2)
    IoPort.output(port2,False)
    time.sleep(delay/2)
    IoPort.output(port1,False)
    IoPort.output(port2,True)
    time.sleep(delay/2)
    IoPort.output(port2,False)
    time.sleep(delay/2)

def sos_S(port1,port2,delay):
    whatPulse_c(port1,port2,delay)
    whatPulse_c(port1,port2,delay)
    whatPulse_c(port1,port2,delay)
    whatPulse_a(port1,port2,delay)
    
def sos_O(port1,port2,delay):
    whatPulse_b(port1,port2,delay)
    whatPulse_c(port1,port2,delay)
    whatPulse_b(port1,port2,delay)
    whatPulse_c(port1,port2,delay)
    whatPulse_b(port1,port2,delay)
    whatPulse_c(port1,port2,delay)
    whatPulse_a(port1,port2,delay)
    
delay = 0.4
port1 = 18
port2 = 23
key7 = 7
key8 = 8
whatPulse_a = pulse_a
whatPulse_b = pulse_b
whatPulse_c = pulse_c

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(port1,IoPort.OUT)
IoPort.setup(port2,IoPort.OUT)
IoPort.setup(key7,IoPort.IN)
IoPort.setup(key8,IoPort.IN)

# main
while True:
    if keyInput(key7):
        whatPulse_a = pulse_a
        whatPulse_b = pulse_b
        whatPulse_c = pulse_c
    elif keyInput(key8):
        whatPulse_a = pulse_A
        whatPulse_b = pulse_B
        whatPulse_c = pulse_C
    else:
        continue
    whatPulse_a(port1,port2,delay)
    whatPulse_a(port1,port2,delay)
    whatPulse_a(port1,port2,delay)
    sos_S(port1,port2,delay)
    sos_O(port1,port2,delay)
    sos_S(port1,port2,delay)
    whatPulse_a(port1,port2,delay)
    whatPulse_a(port1,port2,delay)