import socket
import csv

def run_server(host='192.168.0.180', port=1333):
    with socket.socket() as s:
        try:
            s.bind((host, port))
            s.listen(1)
            conn, addr = s.accept()
            f = open('test.csv', 'w', encoding='utf-8', newline='')
            cw = csv.writer(f)
            while True:
                msg = conn.recv(1024)
                print({msg.decode()})
                cw.writerow({msg.decode()})
        except KeyboardInterrupt:
            f.close()        
            #conn.sendall(msg)
            conn.close()

if __name__ == '__main__':
    run_server()
