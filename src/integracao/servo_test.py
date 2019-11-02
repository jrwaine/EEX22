import RPi.GPIO as GPIO
import time
import ports

srvPin = ports.GPIO_PORT_OUT_PWM_SERVO

fLocked = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(srvPin, GPIO.OUT)
pwm = GPIO.PWM(srvPin, 50)
pwm.start(0)


def setAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(srvPin, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(0.5)
	GPIO.output(srvPin, False)
	pwm.ChangeDutyCycle(0)

def destroy():
    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        while True:
            lock()
            time.sleep(1)
            unlock()
            time.sleep(1)
		
    except KeyboardInterrupt:
        destroy()