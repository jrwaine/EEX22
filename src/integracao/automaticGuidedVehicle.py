from movimentation import Movimentation
from parafusadeira import Parafusadeira

class AGV():
    def __init__(self):
        self.movimentation = Movimentation()
        self.parafusadeira = Parafusadeira()
        # CAMERA ?

    def move(self, distance, position='CIMA'):
        if self.parafusadeira.position != position:
            if position == 'CIMA':
                self.parafusadeira.subir()
            else:
                self.parafusadeira.metade()
        self.movimentation.move(distance)

    def apertar(self, graus):
        self.parafusadeira.descer()
        print('Apertou ', graus)