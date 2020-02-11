import TcpWork
import RcvProt

Eth = TcpWork.TcpWork()
rcvFile = RcvProt.RcvProt()
Eth.Connect('192.168.1.53',20001)
print('connected')
while True:
    btrcv = Eth.Receive()
    for bt in btrcv:
        rcvFile.ByteTrace(bt)
    if len(rcvFile.lst)>1:
        str1 = ''
        for bt in rcvFile.lst:
            str1 = str1 + chr(bt)
        print (str1)
        rcvFile.lst.clear()