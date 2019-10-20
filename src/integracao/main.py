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


def servo_test_loop(cont):
    servo.ChangeDutyCycle(cont)
    time.sleep(0.5)
    if(cont == 0):
        time.sleep(2)

    cont += 1
    if(cont >= 10):
        cont = 0


def motor_paraf_loop():
    # descendo
    gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
    while(gpio.input(pd.GPIO_PORT_IN_FDC_LOWER) == gpio.HIGH):
        continue
    # subindo
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
    while(gpio.input(pd.GPIO_PORT_IN_FDC_HIGHER) == gpio.HIGH):
        continue
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)


def motor_AGV_loop():
    gpio.output(pd.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)
    time.sleep(2)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)
    time.sleep(2.5)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)


try:
    cf.configGPIOs()
    servo = gpio.PWM(pd.GPIO_PORT_OUT_PWM_SERVO, 50)
    servo.start(100)
    cont_buzzer = 0
    cont_servo = 0
    while(1):
        led_test_loop()
        ultrassonic_test_loop()
        motor_paraf_loop()
        # motor_AGV_loop()

except KeyboardInterrupt:
    cf.resetGPIOs()
