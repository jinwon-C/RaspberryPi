import bluetooth
import time
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_sock.bind(("",port))
server_sock.listen(1)
client_sock, address = server_sock.accept()
print "Accepted connction from " +str(address)
#sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#sock.connect(("CC:F3:A5:7C:C3:3F", port))

def send():
    text = raw_input()
    client_sock.send(text)

def receive():
    data = client_sock.recv(1024)
    print("receied [%s]" %data)

while True:
    #text = raw_input()
    #client_sock.send(text)

    #data = client_sock.recv(1024)
    #print( "received [%s]" %data)

    send()
    if client_sock.recv(1024):
        receive()
    time.sleep(0.5)
client_sock.close()
server_sock.close()
sock.close()

