import RPi.GPIO as gpio
import ports
import time

from buzzer import Buzzer
from encoder import Encoder
from ultrassonico import Ultrassonico


class Movimentation:
    def __init__(self):
        self.encoder = Encoder()
        self.ultrassonico = Ultrassonico()
        self.buzzer = Buzzer()
        self.stop()

    def move(self, distance):
        self._restart_threads()

        initial_position = self.encoder.data()

        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        while self.encoder.data() < distance + initial_position:
            if self.ultrassonico.check_can_move():
                self.buzzer.buzz_off()
                gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
                time.sleep(0.050)
                gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
                time.sleep(0.050)
            else:
                self.buzzer.buzz_on()

        self.brake()

    def inicio(self):
        print("\nVoltando o AGV para a posicao de inicio...")
        self._restart_threads()

        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        while self.encoder.data() > 0:
            self.buzzer.buzz_off()
            gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
            time.sleep(0.050)
            gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
            time.sleep(0.050)

        self.brake()
        print("AGV na posicao de inicio!\n")

    def brake(self):
        print("\nFreiando...")
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
        gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
        time.sleep(0.300)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
        gpio.output(ports.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
        gpio.output(ports.GPIO_PORT_OUT_AGV_EN, gpio.LOW)
        print("Freiou!\n")

    def stop(self):
        self.brake()
        print("\nParando as leituras paralelas de movimentacao...")
        self.encoder.stop()
        self.ultrassonico.stop()
        print("Leituras paralelas paradas!\n")

    def _restart_threads(self):
        print("\nReiniciando as leituras paralelas para movimentacao...")
        self.encoder.restart()
        self.ultrassonico.restart()
        print("Leituras paralelas reiniciadas!\n")

    def kill_threads(self):
        self.encoder.kill_thread()
        self.ultrassonico.kill_thread()
