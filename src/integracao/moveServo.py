import RPi.GPIO as gpio
import portDefines as pd
import time


def moveServo(cont):
    servo.ChangeDutyCycle(0)
    time.sleep(2)
    servo.ChangeDutyCycle(cont)
    time.sleep(4)
    # time.sleep(0.5)
    # if(cont == 0):
    #     time.sleep(4)
    # cont += 1 
    # time.sleep(2)
    # if(cont >= 10):
    #     cont = 0
    print("mexeu servo")
    return cont