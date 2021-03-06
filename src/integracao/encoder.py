import RPi.GPIO as gpio
import ports
import time
import threading
import _thread


class Encoder():
    def __init__(self):
        print("Criando encoder...")
        self._stop_event = threading.Event()
        self._kill_self = False
        self.position = 0
        self.state = [(1, 1), (0, 1), (0, 0), (1, 0)]
        self.last_a = 1
        self.last_b = 1
        self.curr_state = [
            i
            for i in range(0, len(self.state))
            if self.state[i] == (self.last_a, self.last_b)
        ][0]
        self.last_state = self.curr_state

    def readEncoder(self):
        self.enc_a = gpio.input(ports.GPIO_PORT_IN_ENC_SIG1)
        self.enc_b = gpio.input(ports.GPIO_PORT_IN_ENC_SIG2)
        time.sleep(0.001)
        if self.enc_a == 1:
            if self.enc_b == 1:
                self.curr_state = 0
            else:
                self.curr_state = 3
        else:
            if self.enc_b == 1:
                self.curr_state = 1
            else:
                self.curr_state = 2

        if self.last_state != self.curr_state:
            if self.curr_state == 0:
                if self.last_state == 3:
                    self.position -= 1
                elif self.last_state == 1:
                    self.position += 1
            self.last_state = self.curr_state

    def run(self):
        print("\nIniciando thread encoder...")
        print("Thread encoder iniciada!\n")
        while not self.stopped():
            self.readEncoder()
        print("Fim da thread do encoder!")

    def data(self):
        return self.position

    def restart(self):
        self._stop_event.clear()
        _thread.start_new_thread (self.run, ())

    def stop(self):
        self._stop_event.set()
        print("\nParando a leitura do encoder...")
        print("Leitura do encoder parada!\n")

    def stopped(self):
        return self._stop_event.is_set()

    def kill_thread(self):
        self.stop()
