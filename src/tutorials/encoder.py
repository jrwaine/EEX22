import RPi.GPIO as GPIO
import time

pin_a = 16
pin_b = 18

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

position = 0

state = [(1, 1), (0, 1), (0, 0), (1, 0)]


last_a = GPIO.input(pin_a)
last_b = GPIO.input(pin_b)

curr_state = [i for i in range(0, len(state)) if state[i] == (last_a, last_b)][0]
last_state = curr_state

while True:
    enc_a = GPIO.input(pin_a)
    enc_b = GPIO.input(pin_b)
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
                position += 1
            elif(last_state == 1):
                position -= 1
        last_state = curr_state
        print(position)

