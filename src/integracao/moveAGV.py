import RPi.GPIO as gpio
import portDefines as pd
import encoder
import time

FORWARD = 1
BACKWARDS = -1

motor = gpio.PWM(pd.GPIO_PORT_OUT_AGV_EN_PWM, 100)
motor.start(0)

def move(distance, velocity, direction=FORWARD):
    if direction == FORWARD:
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
    else:
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)

    initial_position = encoder.data()

    while encoder.data() * direction <= (distance + initial_position) * direction:
        motor.ChangeDutyCycle(velocity)
        gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.HIGH)
    
    stop()

def stop():
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
    motor.ChangeDutyCycle(100)
    gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.HIGH)
    time.sleep(.300)
    gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
    motor.ChangeDutyCycle(0)
    
