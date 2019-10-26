import portDefines as pd
import RPi.GPIO as gpio

class Parafusadeira():
    def __init__(self):
        self.position = None

    def subir(self):
        while(gpio.input(pd.GPIO_PORT_IN_FDC_UPPER) == gpio.HIGH):
            gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable on
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        self.position = 'CIMA'

    def descer(self):
        while(gpio.input(pd.GPIO_PORT_IN_FDC_LOWER) == gpio.HIGH):
            gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable on
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        self.position = 'BAIXO'
    
