import config
from automaticGuidedVehicle import AGV
import globals

try:
    agv = AGV()

    agv.move(20, globals.MEIO)
    agv.apertar(agv.verificar_parafuso())
    agv.move(10, globals.CIMA)
    agv.move(25, globals.MEIO)
    agv.apertar(90)
    agv.inicio()

    agv.kill()

except KeyboardInterrupt:
    agv.kill()
