import config as cf
from moveAGV import Motor
from parafusadeira import Parafusadeira

try:
    para = Parafusadeira()
    para.subir()
    
    # motor = Motor()
    # motor.move(15)
    # motor.move(-15)
    # cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()