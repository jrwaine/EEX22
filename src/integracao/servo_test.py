import sys
import urllib2
import RPi.GPIO as GPIO
import time

srvPin = 3

fLocked = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(srvPin, GPIO.OUT)
pwm = GPIO.PWM(srvPin, 50)
pwm.start(0)

def lock(ev=None):
	global fLocked
	print('locking fLocked=',fLocked)
	if fLocked == False:
		# lock device
		setAngle(110)
		fLocked = True
		print('device locked')
	elif fLocked == True:
		print('device already locked')

def unlock(ev=None):
	global fLocked
	print('unlocking fLocked=', fLocked)
	if fLocked == True:
		# unlock device
		setAngle(15)
		fLocked = False
		print('device unlocked')
	elif fLocked == False:
		print('device already unlocked')

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
        lock()
        time.sleep(15)
        unlock()
		
    except KeyboardInterrupt:
        destroy()