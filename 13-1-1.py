import setup
import RoboPiLib as RPL
import time

sensor_pin = 7
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
    if RPL.digitalRead(sensor_pin) == 1:
        import RoboPiLib as RPL
        import setup
        RPL.servoWrite(0,2000)
        RPL.servoWrite(1,500)

    if RPL.digitalRead(sensor_pin) == 0:
        import RoboPiLib as RPL
        import setup
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,0)
