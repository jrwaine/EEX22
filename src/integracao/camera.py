import portDefines as pd
import RPi.GPIO as gpio
from led import Led

class Camera():
    def __init__(self):
        print('Criando servo')
        self.led = Led()
        
    def verificar(self):
        self.led.acender()

        # processar imagem

        self.led.apagar()
        return 30 # angle