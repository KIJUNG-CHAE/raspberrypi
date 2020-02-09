import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18,gpio.OUT)

def led_on():
    gpio.output(18,True)
    time.sleep(0.4)
    
def led_off():
    gpio.output(18,False)
    time.sleep(0.4)

for i in range(0,10):
    led_on()
    led_off()
    

    
    