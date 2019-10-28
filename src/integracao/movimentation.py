import RPi.GPIO as gpio
import portDefines as pd
import time

from buzzer import Buzzer
from encoder import Encoder
from ultrassonico import Ultrassonico

FORWARD = 1
BACKWARDS = -1

class Movimentation():
    def __init__(self):
        self.encoder = Encoder()
        self.ultrassonico = Ultrassonico()
        self.buzzer = Buzzer()

    def move(self, distance):
        self.restart()

        if distance >= 0:
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        else:
            distance += 3
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
            gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)

        initial_position = self.encoder.data()

        if distance >= 0:
            while self.encoder.data() < distance + initial_position:
                if self.ultrassonico.check_can_move():
                    self.buzzer.buzz_off()
                    gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.HIGH)
                    time.sleep(.050)    
                    gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.LOW)
                    time.sleep(.050)  
                else:
                    self.buzzer.buzz_on()
        else:
            while self.encoder.data() > distance + initial_position:
                gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.HIGH)
                time.sleep(.050)    
                gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.LOW)
                time.sleep(.050)  

        # self.brake()

    def inicio(self):
        self.restart()
        
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        while self.encoder.data() != 0:
            self.buzzer.buzz_off()
            gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.HIGH)
            time.sleep(.050)    
            gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.LOW)
            time.sleep(.050) 
        
        # self.brake()

    def brake(self):
        print("Parando..")
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.HIGH)
        time.sleep(.300)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_AGV_EN_PWM, gpio.LOW)
        print('parou')

    def stop(self):
        # self.brake()
        print('parando a movimentacao')
        self.encoder.stop()
        self.ultrassonico.stop()

    def restart(self):
        if self.encoder.stopped() == True:
            self.encoder.start()
        
        if self.ultrassonico.stopped() == True:
            self.ultrassonico.start()
