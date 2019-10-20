import config as cf
import portDefines as pd
import RPi.GPIO as gpio
import time

def led_test_loop():
# led test
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_LED, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_LED, gpio.LOW)

def buzzer_test_loop():
    buzz()

def buzz():
    gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.LOW)

def ultrassonic_test_loop():
    time.sleep(0.1)
    gpio.output(pd.GPIO_PORT_OUT_ULTR_TRIGG, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(pd.GPIO_PORT_OUT_ULTR_TRIGG, gpio.LOW)

    ini = time.time()
    pulse_end = 0
    pulse_start = 0

    while gpio.input(pd.GPIO_PORT_IN_ULTR_ECHO) == 0:
        pulse_start = time.time()
        if(pulse_start-ini > 2):
            print("Overtime echo 1")
            return

    while gpio.input(pd.GPIO_PORT_IN_ULTR_ECHO) == 1:
        pulse_end = time.time()
        if(pulse_end-pulse_start > 2):
            print("Overtime echo 2")
            return

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance: ", distance, "cm")
    if(distance < 10):
        buzz()
    #time.sleep(1)

try:
    cf.configGPIOs()
    cont_buzzer = 0
    while(1):
        led_test_loop()
        ultrassonic_test_loop()
        '''
        cont_buzzer += 1
        if(cont_buzzer >= 5):
            cont_buzzer = 0
            buzzer_test_loop()
       '''
except KeyboardInterrupt:
    cf.resetGPIOs()
