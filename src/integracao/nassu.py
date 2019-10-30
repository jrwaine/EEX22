import config
from automaticGuidedVehicle import AGV
from ultrassonico import Ultrassonico

try:
    agv = AGV()

    agv.move(20, 'MEIO')
    agv.apertar(agv.verificar_parafuso())
    agv.move(10)
    agv.move(25, 'MEIO')
    agv.apertar(90)
    agv.inicio()

    agv.stop()
    
except KeyboardInterrupt:
    agv.stop()