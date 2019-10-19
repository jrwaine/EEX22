import config as cf
import portDefines as pd
import RPi.GPIO as gpio
import time

def led_teste_loop():
# led teste
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_LED, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_LED, gpio.LOW)

try:
    cf.configGPIOs()
    while(1):
        led_teste_loop()
except KeyboardInterrupt:
    cf.resetGPIOs()