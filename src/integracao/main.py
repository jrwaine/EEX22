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

def buzzer_teste_loop():
    gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(pd.GPIO_PORT_OUT_BUZZER, gpio.LOW)

try:
    cf.configGPIOs()
    cont_buzzer = 0
    while(1):
        led_teste_loop()
        cont_buzzer+=1
        if(cont_buzzer >= 5):
            cont_buzzer = 0
            buzzer_teste_loop()

except KeyboardInterrupt:
    cf.resetGPIOs()