import ports
import RPi.GPIO as gpio
import globals
class Led():
    def __init__(self):
        print('Criando led')
        self.estado = globals.OFF
        
    def acender(self):
        gpio.output(ports.GPIO_PORT_OUT_LED, gpio.HIGH)
        self.estado = globals.ON        

    def apagar(self):
        gpio.output(ports.GPIO_PORT_OUT_LED, gpio.LOW)
        self.estado = globals.OFF   