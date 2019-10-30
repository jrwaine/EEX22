import ports
import RPi.GPIO as gpio
import globals
class Led():
    def __init__(self):
        print('Criando LED...')
        self.estado = globals.OFF
        
    def acender(self):
        print('\nAcendendo LED...')
        gpio.output(ports.GPIO_PORT_OUT_LED, gpio.HIGH)
        self.estado = globals.ON  
        print('\nLED aceso!')      

    def apagar(self):
        print('Apagando LED...')
        gpio.output(ports.GPIO_PORT_OUT_LED, gpio.LOW)
        self.estado = globals.OFF   
        print('\nLED apagado!') 