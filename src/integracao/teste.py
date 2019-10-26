import time
from encoder import Encoder
from threading import Thread

check = False

def func1():
    print ("funn1 started")
    while True:
        if check:
            print ("got permission")
            break

def func2():
    global check
    print ("func2 started")
    time.sleep(2)
    print (enco.data())
    time.sleep(2)
    print (enco.data())

if __name__ == '__main__':
    enco = Encoder()
    func2()
    