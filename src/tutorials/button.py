import RPi.GPIO as gpio
import time

gpio.setwarnings(True)
gpio.setmode(gpio.BOARD)
gpio.setup(3, gpio.IN, pull_up_down=gpio.PUD_DOWN)

while(True):
    if(gpio.input(3) == gpio.HIGH):
        print("ta alto :D")
    else:
        print("ta baixo D:")
    time.sleep(0.5)