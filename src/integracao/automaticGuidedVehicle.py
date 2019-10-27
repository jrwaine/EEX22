from movimentation import Movimentation
from parafusadeira import Parafusadeira
from servo import Servo

class AGV():
    def __init__(self):
        self.parafusadeira = Parafusadeira()
        self.movimentation = Movimentation()
        self.servo = Servo()
        # CAMERA ?

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