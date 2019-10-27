import RPi.GPIO as gpio
import portDefines as pd
import time

from buzzer import Buzzer
from encoder import Encoder
from ultrassonico import Ultrassonico


FORWARD = 1
BACKWARDS = -1

class Movimentation():
    def __init__(self):
        self.encoder = Encoder()
        self.ultrassonico = Ultrassonico()
        self.buzzer = Buzzer()
        self.motor = gpio.PWM(pd.GPIO_PORT_OUT_AGV_EN_PWM, 100)
        self.motor.start(0)

    def move(self, distance):
        if distance >= 0:
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        else:
            distance += 3
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)

        initial_position = self.encoder.data()
        print("Posicao inicial", initial_position)


        if distance >= 0:
            while self.encoder.data() < distance + initial_position:
                if self.ultrassonico.check_can_move():
                    self.buzzer.buzz_off()
                    print("Posicao atual", self.encoder.data())
                    self.motor.ChangeDutyCycle(100)
                    time.sleep(.050)    
                    self.motor.ChangeDutyCycle(0)
                    time.sleep(.050)  
                else:
                    self.buzzer.buzz_on()
        else:
              while self.encoder.data() > distance + initial_position:
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