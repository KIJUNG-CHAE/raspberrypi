import RPi.GPIO as IoPort
import time
import TcpWork

def KeyInput(key):
    if IoPort.input(key) == False:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key)==True:
            break
    time.sleep(0.1)
    return True

keyS = 22
IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(keyS,IoPort.IN)
Tcp = TcpWork.TcpWork()
Tcp.Connect('192.168.1.53',20001)
print('Connected!')
Tcp.Blocking(0)

while True:
    NbStr = Tcp.ReceiveStr()
    if NbStr != None:
        print(NbStr)
    if KeyInput(keyS)==False:
        continue
    StrDta = input("Input Message : ")
    Tcp.SendStr(StrDta)
