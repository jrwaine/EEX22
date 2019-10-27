import config as cf
from automaticGuidedVehicle import AGV

try:
    agv = AGV()

    agv.parafusadeira.subir()
    agv.move(15, 'MEIO')
    agv.move(15)
    agv.apertar(30)
    agv.inicio()
    
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()