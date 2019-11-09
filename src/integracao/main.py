import config
from automaticGuidedVehicle import AGV
from camera import Camera
from communication import Communication
import globals

agv = None

try:
    agv = AGV()

    agv.andar_e_verificar()
    agv.kill()

    comm = Communication()
    comm.try_comunication(agv.get_log())

except KeyboardInterrupt:
    agv.kill()

