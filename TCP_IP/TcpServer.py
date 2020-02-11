import TcpNet
Tcp=TcpNet.TcpNet()
Tcp.Accept('192.168.0.122',20000)
print('Connected......')
while True:
    print(Tcp.ReceiveStr())
    send_data = input('Reply : ')
    Tcp.SendStr(send_data)