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
    gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.LOW)

def ultrassonic_test_loop():
    gpio.output(pd.GPIO_PORT_OUT_ULTR_TRIGG, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(pd.GPIO_PORT_OUT_ULTR_TRIGG, gpio.LOW)

    pulse_end = 0
    pulse_start = 0

    while gpio.input(pd.GPIO_PORT_IN_ULTR_ECHO) == 0:
        pulse_start = time.time()

    while gpio.input(pd.GPIO_PORT_IN_ULTR_ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance: ", distance, "cm")
    # time.sleep(1)

try:
    cf.configGPIOs()
    cont_buzzer = 0
    while(1):
        led_test_loop()
        ultrassonic_test_loop()
        cont_buzzer += 1
        if(cont_buzzer >= 5):
            cont_buzzer = 0
            buzzer_test_loop()

except KeyboardInterrupt:
    cf.resetGPIOs()