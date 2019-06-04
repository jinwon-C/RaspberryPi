import bluetooth
import threading
import time
from bluetooth import *

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

class ChatThread(threading.Thread):
    def __init__ (self, sock, client_info):
        threading.Thread.__init__(self)
        self.sock = sock
        self.client_info = client_info 

    def run(self):
        while True:
            recvData = self.sock.recv(1024)
            print self.client_info, ": received [%s]" % recvData
            
            sendData = raw_input()
            self.sock.send(sendData)
            print self.client_info, ": sent [%s]" % sendData
                    

while True:
    client_socket, client_info = server_socket.accept()
    print (client_info, ": connection accepted")
    Chat = ChatThread(client_socket, client_info)
    Chat.setDaemon(True)
    Chat.start()


client_socket.close()
server_socket.close()


