import RPi.GPIO as GPIO
sw1 = 8
port = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port,GPIO.OUT)
GPIO.setup(sw1,GPIO.IN)
while True:
    rcv = GPIO.input(sw1)
    GPIO.output(port,rcv)