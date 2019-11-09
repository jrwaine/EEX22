import config
from automaticGuidedVehicle import AGV
from camera import Camera
from communication import Communication
from servo import Servo
import globals
import time

agv = None

try:
    # agv = AGV()
    s = Servo()
    s.setAngle(100)
    s.apertar()
    # agv.andar_e_verificar()
    # log = agv.kill()

    # time.sleep(1)

    # print(log)

    # comm = Communication()
    # comm.try_comunication(log)

except KeyboardInterrupt:
    agv.kill()

