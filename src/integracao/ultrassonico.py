import RPi.GPIO as gpio
import ports
import time
import threading
import globals
class Ultrassonico(threading.Thread):
    def __init__(self):
        print('Criando ultrassonico')
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self._kill_self = False
        self.distance = None
        self.close_object = None
        self.start()

    def readUltrassonico(self):
        gpio.output(ports.GPIO_PORT_OUT_ULTR_TRIGG, True)
        time.sleep(0.00001)
        gpio.output(ports.GPIO_PORT_OUT_ULTR_TRIGG, False)

        pulse_end = 0
        pulse_start = 0
        # start = time.time()
        # stop = False
        while gpio.input(ports.GPIO_PORT_IN_ULTR_ECHO) == 0:
            pulse_start = time.time()
            if self.stopped():
                return
        #     if(time.time()-start > globals.LIM_TIME):
        #         print('estorou tempo in')
        #         self.close_object = False
        #         stop = True
        #         continue
        
        # if(stop):
        #     return

        # start = time.time()

        while gpio.input(ports.GPIO_PORT_IN_ULTR_ECHO) == 1:
            pulse_end = time.time()
            if self.stopped():
                return
        #     if(time.time()-start > globals.LIM_TIME):
        #         print('estorou tempo out')
        #         self.close_object = False
        #         stop = True
        #         continue
        
        # if(stop):
        #     return
        
        pulse_duration = pulse_end - pulse_start

        self.distance = round(pulse_duration * 17150, 2)
        
        if self.distance < globals.CLOSE_OBJECT_DISTANCE and self.distance > 0:
            self.close_object = True
            print('tem perto ', self.distance)
        else:
            self.close_object = False

        time.sleep(0.5)

    def run(self):
        print('Iniciando thread ultrassonico')
        while not self._kill_self:
            if not self.stopped():
                self.readUltrassonico()
        
        print('fim da thread do ultra')

    def data(self):
        return self.distance

    def restart(self):
        self._stop_event.clear()
    
    def check_can_move(self):
        return not self.close_object
    
    def stop(self):
        self._stop_event.set()
        print('parando a leitura do ultra')
    
    def kill_thread(self):
        self._kill_self = True

    def stopped(self):
        return self._stop_event.is_set()