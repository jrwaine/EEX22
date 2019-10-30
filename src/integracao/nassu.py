import config
from automaticGuidedVehicle import AGV
from ultrassonico import Ultrassonico
import time

try:
    # agv = AGV()

    ultra = Ultrassonico()
    print('kk ear ', ultra.is_alive())
    while True:
        print('oioi')
        time.sleep(1)

    # for i in range(3):
    #     agv.movimentation.brake()
    #     agv.move(25, 'CIMA')
    #     agv.apertar(agv.verificar_parafuso())
    #     agv.move(10)
    #     agv.move(25, 'MEIO')
    #     agv.apertar(90)
    #     agv.inicio()
    
    #     agv.stop()
    
except KeyboardInterrupt:
    agv.stop()