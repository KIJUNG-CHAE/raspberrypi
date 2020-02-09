import RPi.GPIO as GPIO
import time

def candle(port,on,off):
    global count
    for i in range(0,count):
        GPIO.output(port,True)
        time.sleep(on)
        GPIO.output(port,False)
        time.sleep(off)

port_1 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port_1,GPIO.OUT)

def state1(port_1):
    for i in range(0,40):
        sub = i *0.03/40
        candle(port_1,0.03-sub,sub)
def state2(port_1):
    for i in range(0,40):
        sub = i *0.03/40
        candle(port_1,sub,0.03-sub)
        
count = 30

while True:
    state1(port_1)
    state2(port_1)
