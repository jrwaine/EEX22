import portDefines as pd
import RPi.GPIO as gpio
import time

class Parafusadeira():
    def __init__(self, config=True):
        print('Criando parafusadeira')
        self.position = None
        self.half_duration = None
        self.configured = False
        if config:
            self._config()

    def _config(self):
        if not self.configured:
            self.descer()
            init_time = time.time()
            self.subir()
            self.half_duration = (time.time() - init_time)/2
            self.configured = True

    def metade(self):
        if self.position == 'CIMA':
            gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
            
            if self.configured:
                time.sleep(self.half_duration * .64)
            else:
                time.sleep(1 * .64)

        elif self.position == 'BAIXO':
            gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
            gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
            if self.configured:
                time.sleep(self.half_duration * 1.36)
            else:
                time.sleep(1 * 1.36)
        
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
    
