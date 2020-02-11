import TcpWork
Eth = TcpWork.TcpWork()
Eth.Connect('192.168.1.53',20001)
print('connected')

while True:
    Rece = Eth.Receive()
    Eth.Send(Rece)
    print(Rece.decode("UTF-8"))
    