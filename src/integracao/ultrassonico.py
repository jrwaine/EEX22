import RPi.GPIO as gpio
import ports
import time
import threading
import globals
import _thread


class Ultrassonico():
    def __init__(self):
        print("Criando ultrassonico...")
        self._stop_event = threading.Event()
        self._kill_self = False
        self.distance = None
        self.close_object = None

    def readUltrassonico(self):
        gpio.output(ports.GPIO_PORT_OUT_ULTR_TRIGG, True)
        time.sleep(0.00001)
        gpio.output(ports.GPIO_PORT_OUT_ULTR_TRIGG, False)

        pulse_end = 0
        pulse_start = 0

        while gpio.input(ports.GPIO_PORT_IN_ULTR_ECHO) == 0:
            pulse_start = time.time()
            if self.stopped():
                return

        while gpio.input(ports.GPIO_PORT_IN_ULTR_ECHO) == 1:
            pulse_end = time.time()
            if self.stopped():
                return

        pulse_duration = pulse_end - pulse_start
        self.distance = round(pulse_duration * 17150, 2)

        if self.distance < globals.CLOSE_OBJECT_DISTANCE and self.distance > 0:
            self.close_object = True
            print("Existe um objeto a", self.distance, "cm de distancia do AGV.")
        else:
            self.close_object = False

        time.sleep(0.5)

    def run(self):
        print("\nIniciando thread ultrassonico...")
        print("Thread ultrassonico iniciada!\n")
        while not self.stopped():
            self.readUltrassonico()

        print("Fim da thread do ultrassonico!")

    def restart(self):
        _thread.start_new_thread (self.run)

    def check_can_move(self):
        return not self.close_object

    def stop(self):
        self._stop_event.set()
        print("\nParando a leitura do ultrassonico...")
        print("Leitura do ultrassonico parada!\n")

    def kill_thread(self):
        self._kill_self = True

    def stopped(self):
        return self._stop_event.is_set()
