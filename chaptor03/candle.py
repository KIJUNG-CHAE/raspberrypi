import RPi.GPIO as GPIO
import time

def candle(port,on,off):
    GPIO.output(port,True)
    time.sleep(on)
    GPIO.output(port,False)
    time.sleep(off)

port_1 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port_1,GPIO.OUT)

for i in range(0,40):
    sub = i * 0.0005
    candle(port_1,0.02-sub,0.01)
