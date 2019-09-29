import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(True)
gpio.setup(2, gpio.OUT)
print("led1")

while(1):
    gpio.output(2, gpio.HIGH)
    time.sleep(1)
    gpio.output(2, gpio.LOW)
    time.sleep(1)