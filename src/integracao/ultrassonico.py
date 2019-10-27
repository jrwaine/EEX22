import RPi.GPIO as gpio
import portDefines as pd
import time
import threading

CLOSE_OBJECT_DISTANCE = 10 #cm
LIM_TIME = 2 #seg
class Ultrassonico(threading.Thread):
    def __init__(self):
        print('Criando ultrassonico')
        threading.Thread.__init__(self)
        self.distance = None
        self.close_object = None
        self.start()

    def run(self):
        while True:
            gpio.output(pd.GPIO_PORT_OUT_ULTR_TRIGG, True)
            time.sleep(0.00001)
            gpio.output(pd.GPIO_PORT_OUT_ULTR_TRIGG, False)

            pulse_end = 0
            pulse_start = 0
            start = time.time()
            stop = False
            while gpio.input(pd.GPIO_PORT_IN_ULTR_ECHO) == 0:
                pulse_start = time.time()
                if(time.time()-start > LIM_TIME):
                    print('estou tempo in')
                    self.close_object = False
                    stop = True
                    continue
            
            if(stop):
                continue
            start = time.time()

            while gpio.input(pd.GPIO_PORT_IN_ULTR_ECHO) == 1:
                pulse_end = time.time()
                if(time.time()-start > LIM_TIME):
                    print('estou tempo out')
                    self.close_object = False
                    stop = True
                    continue
            
            if(stop):
                continue
            
            pulse_duration = pulse_end - pulse_start

            self.distance = round(pulse_duration * 17150, 2)
            
            if self.distance < CLOSE_OBJECT_DISTANCE:
                self.close_object = True
                print('tem perto ', self.distance)
            else:
                self.close_object = False

            time.sleep(.01)

    def data(self):
        return self.distance
    
    def check_can_move(self):
        return not self.close_object