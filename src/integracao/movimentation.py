import RPi.GPIO as gpio
import ports
import time

from buzzer import Buzzer
from encoder import Encoder
from ultrassonico import Ultrassonico

class Movimentation():
    def __init__(self):
        self.encoder = Encoder()
        self.ultrassonico = Ultrassonico()
        self.buzzer = Buzzer()

    def move(self, distance):
        print('vai mover')
        self.restart()

        if distance >= 0:
            gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
            gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        else:
            distance += 3
            gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
            gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)

        initial_position = self.encoder.data()

        if distance >= 0:
            while self.encoder.data() < distance + initial_position:
                if self.ultrassonico.check_can_move():
                    self.buzzer.buzz_off()
                    gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
                    time.sleep(.050)    
                    gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
                    time.sleep(.050)  
                else:
                    self.buzzer.buzz_on()
        else:
            while self.encoder.data() > distance + initial_position:
                gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
                time.sleep(.050)    
                gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
                time.sleep(.050)  

        self.brake()

    def inicio(self):
        print('voltando para o inicio')
        self.restart()
        
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        while self.encoder.data() != 0:
            self.buzzer.buzz_off()
            gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
            time.sleep(.050)    
            gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
            time.sleep(.050) 
        
        self.brake()
        self.encoder.kill_thread()
        self.ultrassonico.kill_thread()
        print('ta no inicio')

    def brake(self):
        print("Freiando..")
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
        time.sleep(.300)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
        print("Freiou..")

    def stop(self):
        self.brake()
        print('parando as leituras paralelas de movimentacao')
        self.encoder.stop()
        self.ultrassonico.stop()

    def restart(self):
        print('restartando as leituras para movimentacao')
        self.encoder.restart()
        self.ultrassonico.restart()
