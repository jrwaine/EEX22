import config as cf
from movimentation import Movimentation
from parafusadeira import Parafusadeira
from servo import Servo
from camera import Camera

class AGV():
    def __init__(self):
        self.parafusadeira = Parafusadeira()
        self.movimentation = Movimentation()
        self.servo = Servo()
        self.camera = Camera()

    def move(self, distance, position='CIMA'):
        if self.parafusadeira.position != position:
            if position == 'CIMA':
                self.parafusadeira.subir()
            else:
                self.parafusadeira.metade()
        self.movimentation.move(distance)

    def apertar(self, graus):
        self.movimentation.stop()
        self.parafusadeira.descer()
        self.servo.apertar(graus)
        print('Apertou ', graus, ' graus')

    def inicio(self):
        self.parafusadeira.subir()
        self.movimentation.inicio()

    def verificar_parafuso(self):
        return self.camera.verificar()

    def stop(self):
        cf.resetGPIOs()
        self.movimentation.stop()
        