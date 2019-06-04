from bluetooth import *
import time

client_socket=BluetoothSocket(RFCOMM)

client_socket.connect(("CC:F3:A5:7C:C3:3F",3))

while True:
    text = raw_input()
    client_socket.send(text)
    print "Finished"
    time.sleep(1)
client_socket.close()
