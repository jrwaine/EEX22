import RPi.GPIO as gpio
import portDefines as pd
from encoder import Encoder
import time
import threading

FORWARD = 1
BACKWARDS = -1

class Motor():
    def __init__(self):
        print('Criando motor')
        self.encoder = Encoder()
        self.motor = gpio.PWM(pd.GPIO_PORT_OUT_AGV_EN_PWM, 100)
        self.motor.start(0)

    def move(self, distance, velocity, direction=FORWARD):
        if direction == FORWARD:
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        else:
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        print('oi')
        initial_position = self.encoder.data()
        print("Posicao inicial", initial_position)
        print(str(self.encoder.data() * direction) + ' - ' + str((distance + initial_position) * direction))

        while self.encoder.data() * direction <= (distance + initial_position) * direction:
            print("Posicao atual", self.encoder.data())
            self.motor.ChangeDutyCycle(100)
            time.sleep(.050)    
            self.motor.ChangeDutyCycle(0)
            time.sleep(.050)    

        self.stop()

    def stop(self):
        print("Parando..")
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        self.motor.ChangeDutyCycle(100)
        time.sleep(.300)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        self.motor.ChangeDutyCycle(0)