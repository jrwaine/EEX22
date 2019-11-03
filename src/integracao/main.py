import config
from automaticGuidedVehicle import AGV
from camera import Camera
import globals

agv = None

try:

    # cam = Camera()
    # for i in range(0, 10):
    #     Camera.process()
    #     time.sleep(1)
    agv = AGV()

    agv.andar_e_verificar()

    # agv.camera.verificar()

    # agv.move(25, globals.MEIO)
    # agv.apertar(agv.verificar_parafuso())
    # agv.move(10, globals.CIMA)
    # agv.move(25, globals.MEIO)
    # agv.apertar(90)
    # agv.inicio()

    agv.kill()

except KeyboardInterrupt:
    agv.kill()

