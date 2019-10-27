import portDefines as pd
import RPi.GPIO as gpio
import time

class Buzzer():
    def __init__(self):
        print('Criando buzzer')
        self.state = 'off'

    def buzz_on(self):
        gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.HIGH)
        self.state = 'on'

    def buzz_off(self):
        gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.LOW)
        self.state = 'off'