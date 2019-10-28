import config as cf
import ports
import encoder as ec
import RPi.GPIO as gpio
import time

MIN = 2
MAX = 20
PASSO = 0.5


def led_test_loop():
    time.sleep(0.5)
    gpio.output(ports.GPIO_PORT_OUT_LED, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(ports.GPIO_PORT_OUT_LED, gpio.LOW)

def servo_test_loop(cont):
    print(cont)
    servo.ChangeDutyCycle(cont)
    time.sleep(3)
    cont += PASSO
    if(cont > MAX):
        cont = MIN
    # if(cont == 0):
    #     time.sleep(2)
    # cont += 1  
    # if(cont >= 10):
    #     cont = 0
    print("mexeu")
    return cont

try:
    cf.configGPIOs()
    for x in ports.GPIO_PORTS_OUT:
        gpio.output(x, gpio.LOW)
    servo = gpio.PWM(ports.GPIO_PORT_OUT_PWM_SERVO, 50) #20ms
    servo.start(5) 
    cont_buzzer = 0
    cont_servo = MIN
    while(1):
        #upParafusadeira()
        #downParafusadeira()
        #led_test_loop()
        #ultrassonic_test_loop()
        #motor_paraf_loop()
        #  motor_AGV_loop()
        #servo_test_loop(50) #duty cicle 50%
        cont_servo = servo_test_loop(cont_servo)


except KeyboardInterrupt:
    for x in ports.GPIO_PORTS_OUT:
        gpio.output(x, gpio.LOW)
    cf.resetGPIOs()
