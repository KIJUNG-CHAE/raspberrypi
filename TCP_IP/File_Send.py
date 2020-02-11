import os
import struct
import TcpWork
import SndProt

Tcp=TcpWork.TcpWork()
Tcp.Connect('192.168.1.53',20001)
Prot = SndProt.SndProt()

while True:
    FileName = input("Input File Name : ")
    if os.path.isfile(FileName) == False:
        print(FileName,' is not file name. Try Again!!!')
        continue
    fle = open(FileName,'rb')
    btfile = fle.read()
    fle.close()
    bDta = Prot.pFileSend(FileName,btfile)
    Tcp.Send(bDta)
    