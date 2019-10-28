import RPi.GPIO as gpio
import ports
import time

servo = gpio.PWM(ports.GPIO_PORT_OUT_PWM_SERVO, 50) #50hz
servo.start(0) 

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