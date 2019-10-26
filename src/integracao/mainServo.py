import config as cf
import moveServo as servo
import RPi.GPIO as gpio
try:
    cont_servo = 50
    print("tentativa sucedida")
    while(1):
        cont_servo = servo.moveServo(cont_servo)

except KeyboardInterrupt:
    cf.resetGPIOs()