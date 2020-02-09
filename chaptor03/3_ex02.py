import RPi.GPIO as GPIO
import time

port_1=18
port_2=23
port_3=24
port_4=25
delay=0.4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port_1,GPIO.OUT)
GPIO.setup(port_2,GPIO.OUT)
GPIO.setup(port_3,GPIO.OUT)
GPIO.setup(port_4,GPIO.OUT)

def state_1(delay):
    GPIO.output(port_1,True)
    GPIO.output(port_4,False)
    time.sleep(delay)
    
def state_2(delay):
    GPIO.output(port_2,True)
    GPIO.output(port_1,False)
    time.sleep(delay)

def state_3(delay):
    GPIO.output(port_3,True)
    GPIO.output(port_2,False)
    time.sleep(delay)
    
def state_4(delay):
    GPIO.output(port_4,True)
    GPIO.output(port_3,False)
    time.sleep(delay)
    
while(True):
    state_1(delay)
    state_2(delay)        
    state_3(delay)
    state_4(delay)
            