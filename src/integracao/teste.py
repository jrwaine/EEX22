from moveAGV import Motor

try:
    motor = Motor()
    print('ta')
    motor.move(15, 60)

except:
    pass