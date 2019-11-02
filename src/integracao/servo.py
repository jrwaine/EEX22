import RPi.GPIO as gpio
import ports
import time
import globals


class Servo:
    def __init__(self):
        print("Criando servo...")
        self.position = globals.MIN
        self.pwm = gpio.PWM(ports.GPIO_PORT_OUT_PWM_SERVO, 50)
        self.pwm.start(0)
        self.setAngle(180)
        time.sleep(2)
        self.setAngle(0)
        time.sleep(2)

    def apertar(self):
        time.sleep(0.5)
        self.setAngle(0)
        print("Apertou!")
        
    def setAngle(self, angle):
        duty = 10*angle/180 + 2.5
        gpio.output(ports.GPIO_PORT_OUT_PWM_SERVO, True)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        gpio.output(ports.GPIO_PORT_OUT_PWM_SERVO, False)
        self.pwm.ChangeDutyCycle(0)

        