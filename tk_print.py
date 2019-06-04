import threading

def hello():
    while 1:
        print("hello")

t = threading.Thread(target=hello)
t.start()
