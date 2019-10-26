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
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
    else:
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)

    initial_position = encoder.data()
    print("Posicao inicial", initial_position)
    print(str(encoder.data() * direction) + ' - ' + str((distance + initial_position) * direction))

    while encoder.data() * direction <= (distance + initial_position) * direction:
        print("Posicao atual", encoder.data())
        motor.ChangeDutyCycle(100)
        time.sleep(.050)    
        motor.ChangeDutyCycle(0)
        time.sleep(.050)    

    stop()

def stop():
    print("Parando..")
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
    motor.ChangeDutyCycle(100)
    time.sleep(.300)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
    motor.ChangeDutyCycle(0)
    
