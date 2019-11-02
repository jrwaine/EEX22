# Servo1.py
import RPi.GPIO as gpio
import ports
import time
import globals
import config
import pigpio

fPWM = 50  # Hz (not higher with software PWM)
a = 12.5
b = 2.5


config.resetGPIOs()
config.configGPIOs()
pi = pigpio.pi()

def setup():
    global pwm
    #pwm = gpio.PWM(ports.GPIO_PORT_OUT_PWM_SERVO, fPWM)
    pi.set_PWM_frequency(24, 50)
    print("frequency", pi.get_PWM_frequency(24))
    pi.set_PWM_dutycycle(24, 0)


def setDirection(direction):
    duty = ((a-b) / 180 * direction + b)/100*255
    #pwm.ChangeDutyCycle(duty)
    pi.set_PWM_dutycycle(24, int(duty))
    print("direction =", direction, "-> duty =", duty)
    time.sleep(2)  # allow to settle


print("starting")
setup()
print(pi.get_mode(ports.GPIO_PORT_OUT_PWM_SERVO))
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0
setDirection(0)

config.resetGPIOs()

print("done")
