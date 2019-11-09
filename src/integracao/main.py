import config
from automaticGuidedVehicle import AGV
from camera import Camera
from communication import Communication
import globals

agv = None

try:
    agv = AGV()

    agv.andar_e_verificar()
    comm = Communication()
    comm.try_comunication(agv.get_log())

    agv.kill()

except KeyboardInterrupt:
    agv.kill()

