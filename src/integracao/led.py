import portDefines as pd
import RPi.GPIO as gpio

ON = 1
OFF = 0

class Led():
    def __init__(self):
        print('Criando led')
        self.estado = OFF
        
    def acender(self):
        gpio.output(pd.GPIO_PORT_OUT_LED, gpio.HIGH)
        self.estado = ON        

    def apagar(self):
        gpio.output(pd.GPIO_PORT_OUT_LED, gpio.LOW)
        self.estado = OFF   