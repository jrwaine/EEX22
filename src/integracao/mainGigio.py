import config as cf
from moveAGV import Motor

try:
    motor = Motor()
    motor.move(15, 60)
    motor.move(15, 60)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()