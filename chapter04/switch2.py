import RPi.GPIO as IoPort
sw1 = 8
end = 7
port = 18
IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(port,IoPort.OUT)
IoPort.setup(sw1,IoPort.IN)
IoPort.setup(end,IoPort.IN)

count = 0
while count == 0:
    rcv = IoPort.input(sw1)
    IoPort.output(port,rcv)
    if IoPort.input(end) == False:
        count = 1
IoPort.output(port,False)