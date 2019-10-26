import config as cf
import moveAGV as motor

try:
    motor.move(15, 60)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()