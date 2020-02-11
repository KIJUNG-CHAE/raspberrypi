import TcpNet
Tcp = TcpNet.TcpNet()
Tcp.Connect('192.168.1.53',20001)
print('Connection.....')
while True:
    send_data=input('message : ')
    Tcp.SendStr(send_data)
    print(Tcp.ReceiveStr())