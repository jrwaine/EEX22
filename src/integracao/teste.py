from threading import Thread
import time

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
    check = True
    time.sleep(2)
    check = False

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()