import ports
# import RPi.GPIO as gpio
from led import Led

class Camera():
    def __init__(self):
        print('Criando camera...')
        self.led = Led()
        
    def verificar(self):
        self.led.acender()
        print('\nProcessando a imagem...')

        # processar imagem
        print('Imagem processada!\n')
        self.led.apagar()
        return 30 # angle