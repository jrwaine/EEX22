import config as cf
import moveAGV as motor

try:
    motor.move(20, 5)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()