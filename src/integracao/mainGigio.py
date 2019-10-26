import config as cf
from moveAGV import Motor
from parafusadeira import Parafusadeira

try:
    para = Parafusadeira()
    motor = Motor()

    para.descer()
    motor.move(15)

    para.subir()
    motor.move(15)
    motor.move(-30)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()