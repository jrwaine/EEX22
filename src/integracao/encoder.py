import RPi.GPIO as gpio
import portDefines as pd
import time
from threading import Thread

position = 0
state = [(1, 1), (0, 1), (0, 0), (1, 0)]

last_a = 1
last_b = 1

curr_state = [i for i in range(0, len(state)) if state[i] == (last_a, last_b)][0]
last_state = curr_state
position = 0

def data():
    return position

def check():
    global last_a
    global last_b
    global last_state
    global position
    print("TA NA THREAD ", position)
    enc_a = gpio.input(pd.GPIO_PORT_IN_ENC_SIG1)
    enc_b = gpio.input(pd.GPIO_PORT_IN_ENC_SIG2)
    time.sleep(0.001)
    if(enc_a == 1):
        if(enc_b == 1):
            curr_state = 0
        else:
            curr_state = 3
    else:
        if(enc_b == 1):
            curr_state = 1
        else:
            curr_state = 2
 
    if(last_state != curr_state):
        if(curr_state == 0):
            if(last_state == 3):
                position -= 1
            elif(last_state == 1):
                position += 1
        last_state = curr_state

Thread(target = check).start()