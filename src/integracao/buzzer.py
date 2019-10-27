import portDefines as pd
import RPi.GPIO as gpio
import time

ON = 1
OFF = 0

class Buzzer():
    def __init__(self):
        print('Criando buzzer')
        self.state = OFF

    def buzz_on(self):
        gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.HIGH)
        self.state = ON

    def buzz_off(self):
        gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.LOW)
        self.state = OFF