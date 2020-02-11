import RPi.GPIO as IoPort
import time
import os
import TcpWork
import SndProt
import RcvProt
#key input
def KeyInput(key):
    if IoPort.input(key) == False:
        return False
    time.sleep(0.1)
    while True:
        if IoPort.input(key) == True:
            break
    time.sleep(0.1)
    return True
#key num
key22 = 22
key27 = 27
#set
IoPort.setmode(IoPort.BCM)
IoPort.setwarnings(False)
IoPort.setup(key22,IoPort.IN)
IoPort.setup(key27,IoPort.IN)
#object
Tcp = TcpWork.TcpWork()
rcvFile = RcvProt.RcvProt()
sndFile = SndProt.SndProt()

Tcp.Connect('192.168.1.53',20001)
print("Connected")
Tcp.Blocking(0)

while True:
    if KeyInput(key22)==True:
        sndmsg = input('message : ')
        Tcp.SendStr(sndmsg)
        
    if KeyInput(key27)==True:
        FileName = input("Input File Name : ")
        if os.path.isfile(FileName) == False:
            print(FileName,' is not file name. Try Again!!!')
            continue
        fle = open(FileName,'rb')
        btfile = fle.read()
        fle.close()
        bDta = sndFile.pFileSend(FileName,btfile)
        Tcp.Send(bDta)

    btrcv = Tcp.Receive()
    if btrcv == None:
        continue
    for bt in btrcv:
        rcvFile.ByteTrace(bt)
    if len(rcvFile.lst)>1:
        str1 = ''
        for bt in rcvFile.lst:
            str1 = str1 + chr(bt)
        print (str1)
        rcvFile.lst.clear()
    