import RPi.GPIO as GPIO
import time

led_1=18
led_2=23
delay=0.4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)

