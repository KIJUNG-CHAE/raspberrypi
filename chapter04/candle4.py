import RPi.GPIO as IoPort
import time

def SlowOnOff(Switch):
    global Bool
    
    if Bool == False:
        for i in range(1,40):
            IoPort.output(Led,False)
            time.sleep(0.02-0.0005*i)
            IoPort.output(Led,True)
            time.sleep(0.0005*i)
        
        time.sleep(0.1)
        Bool = True
    else:
        for i in range(1,40):
            IoPort.output(Led,True)
            time.sleep(0.02-0.0005*i)
            IoPort.output(Led,False)
            time.sleep(0.0005*i)
        
        time.sleep(0.1)
        Bool = False
            

Switch = 7
Led = 24
Bool = False

IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(Switch,IoPort.IN)
IoPort.setup(Led,IoPort.OUT)
IoPort.add_event_detect(Switch,IoPort.FALLING,callback=SlowOnOff)

    