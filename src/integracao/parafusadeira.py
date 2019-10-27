import portDefines as pd
import RPi.GPIO as gpio
import time

class Parafusadeira():
    def __init__(self):
        print('Criando parafusadeira')
        self.position = None
        self.half_duration = None
        self._config()

    def _config(self):
        self.subir()
        self.descer()
        init_time = time.time()
        self.subir()
        self.half_duration = (time.time() - init_time)/2

    def metade(self):
        if self.position == 'CIMA':
            gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
            time.sleep(self.half_duration * .7)

        elif self.position == 'BAIXO':
            gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
            time.sleep(self.half_duration * 1.3)
        
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable on
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        self.position = 'MEIO'

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
    
