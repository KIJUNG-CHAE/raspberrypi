import RPi.GPIO as GPIO
import time
led_1 = 18
led_2 = 25
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)

def case_1(port1,port2,delay):
    GPIO.output(port2,False)
    GPIO.output(port1,True)
    time.sleep(delay)
    GPIO.output(port1,False)
    time.sleep(delay)
    
def case_2(port1,port2,delay):
    GPIO.output(port2,True)
    GPIO.output(port1,True)
    time.sleep(delay)
    GPIO.output(port1,False)
    time.sleep(delay)
    
def case_3(port1,port2,delay):
    GPIO.output(port1,True)
    GPIO.output(port2,True)
    time.sleep(delay)
    GPIO.output(port1,False)
    GPIO.output(port2,False)
    time.sleep(delay)
    
def send_S(port1,port2,delay):
    case_2(port1,port2,delay)
    case_1(port1,port2,delay)
    case_2(port1,port2,delay)
    case_1(port1,port2,delay)
    case_2(port1,port2,delay)
    case_1(port1,port2,delay)
    case_1(port1,port2,delay)
    case_1(port1,port2,delay)
    
def send_O(port1,port2,delay):
    case_2(port1,port2,delay)
    case_2(port1,port2,delay)
    case_2(port1,port2,delay)
    case_1(port1,port2,delay)
    case_2(port1,port2,delay)
    case_2(port1,port2,delay)
    case_2(port1,port2,delay)
    case_1(port1,port2,delay)
    case_2(port1,port2,delay)
    case_2(port1,port2,delay)
    case_2(port1,port2,delay)
    case_1(port1,port2,delay)
    case_1(port1,port2,delay)
    case_1(port1,port2,delay)
    
for i in range(0,10):
    
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)

    send_S(led_1,led_2,0.2)
    send_O(led_1,led_2,0.2)
    send_S(led_1,led_2,0.2)

    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
    case_1(led_1,led_2,0.2)
