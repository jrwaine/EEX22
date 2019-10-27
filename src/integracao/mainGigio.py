import config as cf
from automaticGuidedVehicle import AGV

try:
    agv = AGV()

    agv.move(25, 'MEIO')
    agv.apertar(30)
    agv.move(15)
    agv.inicio()
    

    
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()