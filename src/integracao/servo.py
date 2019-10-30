import RPi.GPIO as gpio
import ports
import globals

class Servo():
    def __init__(self):
        print('Criando servo...')
        self.position = globals.MIN
     
        
    def apertar(self, graus):
        print('Preparando para apertar', graus, 'graus...')

        # TODO

        print('Apertou', graus, 'graus!')
