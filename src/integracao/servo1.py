# Servo1.py
import RPi.GPIO as gpio
import ports
import time
import globals
import config

P_SERVO = 22  # adapt to your wiring
fPWM = 50  # Hz (not higher with software PWM)
a = 10
b = 2


def setup():
    global pwm
    pwm = gpio.PWM(ports.GPIO_PORT_OUT_PWM_SERVO, fPWM)
    pwm.start(0)


def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)
    time.sleep(1)  # allow to settle


print("starting")
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0
setDirection(0)
gpio.cleanup()
print("done")
