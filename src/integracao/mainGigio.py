import config as cf
from automaticGuidedVehicle import AGV
from ultrassonico import Ultrassonico
import time

try:
    # agv = AGV()

    # agv.move(25, 'MEIO')
    # agv.apertar(30)
    # agv.move(15)
    # agv.inicio()
    ultra = Ultrassonico()
    time.sleep(20)

    
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()