import config as cf
import moveAGV as motor
import encoder
from threading import Thread

th = Thread(target = encoder.check)
print(th)
th.start()

try:
    motor.move(15, 60)
    cf.resetGPIOs()

except KeyboardInterrupt:
    cf.resetGPIOs()