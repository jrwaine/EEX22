import config as cf
from movimentation import Movimentation
from parafusadeira import Parafusadeira
from servo import Servo
from camera import Camera
import globals


class AGV:
    def __init__(self):
        print("Criando o AGV...")
        self.movimentation = Movimentation()
        self.servo = Servo()
        self.camera = Camera()
        self.parafusadeira = Parafusadeira()
        
    def move(self, distance, parafusadeira_position):
        if self.parafusadeira.position != parafusadeira_position:
            if parafusadeira_position == globals.CIMA:
                self.parafusadeira.subir()
            else:
                self.parafusadeira.metade()
        self.movimentation.move(distance)

    def apertar(self, graus):
        self.movimentation.stop()
        print("Preparando para apertar", graus, "graus...")
        self.servo.setAngle(graus)
        self.parafusadeira.descer()
        self.servo.apertar()

    def inicio(self):
        self.parafusadeira.subir()
        self.movimentation.inicio()

    def verificar_parafuso(self):
        return self.camera.verificar()

    def kill(self):
        print("\nEncerrando as atividades do AGV ...")
        self.movimentation.kill_threads()
        cf.resetGPIOs()
        print("Atividade do AGV encerradas!\n")
