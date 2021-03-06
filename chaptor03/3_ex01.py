import RPi.GPIO as GPIO
import time

led_1=18
led_2=23
delay=0.4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)

def case_1(led_1,led_2,delay):
    GPIO.output(led_1,False)
    GPIO.output(led_2,False)
    time.sleep(delay)
    
def case_2(led_1,led_2,delay):
    GPIO.output(led_1,True)
    GPIO.output(led_2,False)
    time.sleep(delay)
    
def case_3(led_1,led_2,delay):
    GPIO.output(led_1,False)
    GPIO.output(led_2,True)
    time.sleep(delay)
    
def case_4(led_1,led_2,delay):
    GPIO.output(led_1,True)
    GPIO.output(led_2,True)
    time.sleep(delay)

for i in range(0,10):
    case_1(led_1,led_2,delay)
    case_2(led_1,led_2,delay)
    case_4(led_1,led_2,delay)
    case_3(led_1,led_2,delay)
    case_1(led_1,led_2,delay)
    case_1(led_1,led_2,delay)
    case_1(led_1,led_2,delay)  
    
    
    