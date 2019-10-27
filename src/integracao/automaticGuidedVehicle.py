from movimentation import Movimentation
from parafusadeira import Parafusadeira

class AGV():
    def __init__(self):
        self.parafusadeira = Parafusadeira()
        self.movimentation = Movimentation()
        # CAMERA ?

    def move(self, distance, position='CIMA'):
        if self.parafusadeira.position != position:
            if position == 'CIMA':
                self.parafusadeira.subir()
            else:
                self.parafusadeira.metade()
        self.movimentation.move(distance)

    def apertar(self, graus):
        self.movimentation.kill()
        self.parafusadeira.descer()
        print('Apertou ', graus)

    def inicio(self):
        self.parafusadeira.subir()
        self.movimentation.inicio()