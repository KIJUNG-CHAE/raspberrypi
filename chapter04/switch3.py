import RPi.GPIO as IoPort
import time
IoPort.setmode(IoPort.BCM)

def state(st):
    global sta
    if st == 1:
        IoPort.output(port1,True)
        IoPort.output(port2,False)
    elif st == 2:
        IoPort.output(port1,False)
        IoPort.output(port2,True)
    elif st == 3:
        IoPort.output(port1,True)
        IoPort.output(port2,True)
    elif st == 4:
        IoPort.output(port1,False)
        IoPort.output(port2,False)
        sta = 0

swt=8
end=7
port1=18
port2=23
IoPort.setwarnings(False)
IoPort.setup(swt,IoPort.IN)
IoPort.setup(end,IoPort.IN)
IoPort.setup(port1,IoPort.OUT)
IoPort.setup(port2,IoPort.OUT)

sta = 1

while sta <= 4:
    state(sta)
    while True:
        if IoPort.input(swt) == False:
            break
    time.sleep(0.3)
    while True:
        if IoPort.input(swt) == True:
            break
    time.sleep(0.3)
    sta += 1

        
