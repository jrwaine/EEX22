import config
from automaticGuidedVehicle import AGV
from camera import Camera
from communication import Communication
import globals
import time

agv = None

try:
    agv = AGV()

    agv.andar_e_verificar()
    log = agv.kill()

    time.sleep(1)

    print(log)

    comm = Communication()
    comm.try_comunication(log)

except KeyboardInterrupt:
    agv.kill()

