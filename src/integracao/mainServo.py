import config as cf
import moveServo as servo

try:
    servo = gpio.PWM(pd.GPIO_PORT_OUT_PWM_SERVO, 50) #50hz
    servo.start(50)
    cont_servo = 50
    while(1):
        cont_servo = moveServo(cont_servo)

except KeyboardInterrupt:
    cf.resetGPIOs()