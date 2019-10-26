import config as cf
import moveAGV as motor

try:
    motor.move(30, 20)

except KeyboardInterrupt:
    
    cf.resetGPIOs()