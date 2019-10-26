import config as cf
from moveAGV import Motor

try:
    motor = Motor()
    motor.move(15)
    motor.move(-15)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()