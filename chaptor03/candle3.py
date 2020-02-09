import RPi.GPIO as GPIO
import time

def candle(port,on,off):
    GPIO.output(port,True)
    time.sleep(on)
    GPIO.output(port,False)
    time.sleep(off)

port_1 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port_1,GPIO.OUT)

def slow_on_off():
    for i in range(0,100):
        sub = i * 0.0002
        candle(port_1,sub,0.02-sub)
    for i in range(0,100):
        sub = i * 0.0002
        candle(port_1,0.02-sub,sub)

while(True):
    slow_on_off()
    