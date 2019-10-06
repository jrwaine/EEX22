import RPi.GPIO as gpio
import time

gpio.cleanup()
portMotorVert = (16, 18)
enableMotorVert = 12
portMotorAGV = (22, 24)
enableMotorAGV = 26

portsOUT = [12, 16, 18, 22, 24, 26]

#signalMotorA = [gpio.LOW, gpio.LOW]
#signalMotorB = [gpio.LOW, gpio.LOW]

gpio.setwarnings(True)
gpio.setmode(gpio.BOARD)

for i in portsOUT:
    gpio.setup(i, gpio.OUT)

while(True):
    a = 0
'''
gpio.output(12, gpio.HIGH)
gpio.output(26, gpio.HIGH)

while(True):
    gpio.output(portMotorVert[0], gpio.LOW)
    gpio.output(portMotorVert[1], gpio.HIGH)
    gpio.output(portMotorAGV[0], gpio.LOW)
    gpio.output(portMotorAGV[1], gpio.HIGH)
    time.sleep(1)
    gpio.output(portMotorVert[1], gpio.LOW)
    gpio.output(portMotorVert[0], gpio.HIGH)
    gpio.output(portMotorAGV[1], gpio.LOW)
    gpio.output(portMotorAGV[0], gpio.HIGH)
    time.sleep(1)
'''
gpio.cleanup()

