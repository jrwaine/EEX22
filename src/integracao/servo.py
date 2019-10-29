# import RPi.GPIO as gpio
import ports
import time
import globals

class Servo():
    def __init__(self):
        print('Criando servo')
        # self._pwm = gpio.PWM(ports.GPIO_PORT_OUT_PWM_SERVO, 50) #20ms
        # self._pwm.start(0) 
        self.position = globals.MIN
        
    def apertar(self, graus):
        print('posicionando em', graus, 'graus')
        # while self.position != int(graus * globals.PASSO) + globals.MIN:
        #     self.position += globals.PASSO
        #     if(self.position > globals.MAX):
        #         self.position = globals.MIN
        #     self._pwm.ChangeDutyCycle(self.position)
        #     time.sleep(.8)
        
        # print('trazendo para', 0, 'graus')
        # while self.position != globals.MIN:
        #     self.position -= globals.PASSO
        #     self._pwm.ChangeDutyCycle(self.position)
        #     time.sleep(.8)

        print('apertou')
        # self._pwm.ChangeDutyCycle(0)