import portDefines as pd
import RPi.GPIO as gpio
import time

MIN = 2
MAX = 20
PASSO = .2 # (MAX - MIN)/90

class Servo():
    def __init__(self, config=True):
        print('Criando servo')
        self._pwm = gpio.PWM(pd.GPIO_PORT_OUT_PWM_SERVO, 50) #20ms
        self._pwm.start(MIN) 
        self.position = MIN
        
    def apertar(self, graus):
        while self.position != int(graus * PASSO) + MIN:
            self.position += PASSO
            if(self.position > MAX):
                self.position = MIN
            self._pwm.ChangeDutyCycle(self.position)
            time.sleep(.8)
        
        while self.position != MIN:
            self.position -= PASSO
            self._pwm.ChangeDutyCycle(self.position)
            time.sleep(.8)