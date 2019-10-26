import config as cf
import moveAGV as motor

try:
    motor.move(20, 1)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()