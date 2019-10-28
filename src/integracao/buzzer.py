import ports
import RPi.GPIO as gpio
import time
import globals

class Buzzer():
    def __init__(self):
        print('Criando buzzer')
        self.state = globals.OFF

    def buzz_on(self):
        gpio.output(ports.GPIO_PORT_OUT_BUZZER, gpio.HIGH)
        self.state = globals.ON

    def buzz_off(self):
        gpio.output(ports.GPIO_PORT_OUT_BUZZER, gpio.LOW)
        self.state = globals.OFF