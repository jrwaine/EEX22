import config as cf
import portDefines as pd
import encoder as ec
import RPi.GPIO as gpio
import time


def upParafusadeira():
    if(gpio.input(pd.GPIO_PORT_IN_FDC_UPPER) == gpio.HIGH): #chave desapertada
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        time.sleep(1)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable off
        print("parafusadeira parada no topo")
    else:
        print("ja esta no topo")

def downParafusadeira():
    if(gpio.input(pd.GPIO_PORT_IN_FDC_LOWER) == gpio.HIGH): #chave desapertada
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
        while(gpio.input(pd.GPIO_PORT_IN_FDC_LOWER) == gpio.HIGH): #enquanto chave desapertada
            continue
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
        gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
        print("desabilitando enable")
        gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.LOW) #enable off
        print("parafusadeira parada embaixo")
    else:
        print("ja esta embaixo")

def led_test_loop():
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




def motor_paraf_loop():
    # descendo
    gpio.output(pd.GPIO_PORT_OUT_PARAF_EN, gpio.HIGH) #enable on
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
    while(gpio.input(pd.GPIO_PORT_IN_FDC_LOWER) == gpio.HIGH):
        continue
    '''
    time.sleep(1)
    cont = 1
    while(cont != 0):
        cont = servo_test_loop(cont)
    time.sleep(1)
    '''
    # subindo
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.LOW)
    while(gpio.input(pd.GPIO_PORT_IN_FDC_UPPER) == gpio.HIGH):
        continue
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_PARAF_SIG2, gpio.HIGH)
    time.sleep(4)


def motor_AGV_loop():
    gpio.output(pd.GPIO_PORT_OUT_AGV_EN, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.HIGH)

    ini = time.time()
    position = ec.encoder()
    while(time.time()-ini < 2):
        res = ec.encoder()
        if(res != position):
            print(res)
            position = res
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.HIGH)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)

    ini = time.time()
    position = ec.encoder()
    while(time.time()-ini < 4):
        res = ec.encoder()
        if(res != position):
            print(res)
            position = res

    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG1, gpio.LOW)
    gpio.output(pd.GPIO_PORT_OUT_AGV_SIG2, gpio.LOW)

def servo_test_loop(cont):
    servo.ChangeDutyCycle(cont)
    time.sleep(2)
    # if(cont == 0):
    #     time.sleep(2)
    # cont += 1  
    # if(cont >= 10):
    #     cont = 0
    print("mexeu")
    return cont

try:
    cf.configGPIOs()
    for x in pd.GPIO_PORTS_OUT:
        gpio.output(x, gpio.LOW)
    servo = gpio.PWM(pd.GPIO_PORT_OUT_PWM_SERVO, 50) #20ms
    servo.start(5) 
    cont_buzzer = 0
    cont_servo = 7.5
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
    for x in pd.GPIO_PORTS_OUT:
        gpio.output(x, gpio.LOW)
    cf.resetGPIOs()
