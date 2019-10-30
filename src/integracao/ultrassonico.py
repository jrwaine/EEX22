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
        self.distance = None
        self.close_object = None
        self.start()

    def readUltrassonico(self):
        gpio.output(ports.GPIO_PORT_OUT_ULTR_TRIGG, True)
        time.sleep(0.00001)
        gpio.output(ports.GPIO_PORT_OUT_ULTR_TRIGG, False)

        pulse_end = 0
        pulse_start = 0
        start = time.time()
        stop = False
        while gpio.input(ports.GPIO_PORT_IN_ULTR_ECHO) == 0:
            pulse_start = time.time()
        #     if(time.time()-start > globals.LIM_TIME):
        #         print('estorou tempo in')
        #         self.close_object = False
        #         stop = True
        #         continue
        
        # if(stop):
        #     return

        start = time.time()

        while gpio.input(ports.GPIO_PORT_IN_ULTR_ECHO) == 1:
            pulse_end = time.time()
        #     if(time.time()-start > globals.LIM_TIME):
        #         print('estorou tempo out')
        #         self.close_object = False
        #         stop = True
        #         continue
        
        # if(stop):
        #     return
        
        pulse_duration = pulse_end - pulse_start

        self.distance = round(pulse_duration * 17150, 2)/2
        
        if self.distance < globals.CLOSE_OBJECT_DISTANCE and self.distance > 0:
            self.close_object = True
            print('tem perto ', self.distance)
        else:
            self.close_object = False

        time.sleep(.01)

    def run(self):
        # try:
        #     self.start()
        # except:
        #     pass
        print('Iniciando thread ultrassonico')
        while not self.stopped():
            self.readUltrassonico()
        self._stop_event.clear()
        print('parou a thread do ultra', self.stopped())

    def data(self):
        return self.distance
    
    def check_can_move(self):
        return not self.close_object
    
    def stop(self):
        self._stop_event.set()
        print('tentando parar a thread do ultra')

    def stopped(self):
        return self._stop_event.is_set()