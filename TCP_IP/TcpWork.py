import socket
class TcpWork:
    def __init__(self):
        self.com_socket = socket.socket()
        self.Connection=self.com_socket
    def Accept(self,IP,Port):
        self.com_socket.bind((IP,Port))
        self.com_socket.listen(10);
        self.Connection, self.address = self.com_socket.accept()
    def Connect(self,IP,Port):
        self.com_socket.connect((IP,Port))
    def Send(self,bdta):
        self.Connection.send(bdta)
    def SendStr(self,Str1):
        self.Connection.send(bytes(Str1,"UTF-8"))
    def Receive(self):
        try:
            return self.Connection.recv(4096)
        except:
            return None
    def ReceiveStr(self):
        try:
            return self.Connection.recv(4096).decode("UTF-8")
        except:
            return None
    def Blocking(self,Tme): #Tme ==0 nonblocking ture
        self.Connection.setblocking(Tme)

