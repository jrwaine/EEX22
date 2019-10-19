import RPi.GPIO as GPIO
import time
import config as cf
import portDefines as pd
cf.configGPIOs()

TRIG = pd.GPIO_PORT_OUT_ULTR_TRIGG
ECHO = pd.GPIO_PORT_IN_ULTR_ECHO
print("medindo")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("esperando")
time.sleep(2)

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_end = 0
    pulse_start = 0

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distancia: ", distance, "cm")
    time.sleep(1)

cf.resetGPIOs()

