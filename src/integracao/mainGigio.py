import config as cf
import moveAGV as motor

try:
    motor.move(20, 100)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()