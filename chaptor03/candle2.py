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

for i in range(0,40):
    count = 10+i
    sub = i * 0.0005
    candle(port_1,0.02-sub,0.01)

