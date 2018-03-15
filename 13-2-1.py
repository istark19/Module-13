import setup
import RoboPiLib as RPL

sensor_pin = 17
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  while RPL.digitalRead(sensor_pin) == 1:
    RPL.servoWrite(0,500)
    RPL.servoWrite(1,2000)
  while RPL.digitalRead(sensor_pin)== 0:
    first_time == time.time()
    while 1 >= time.time() - first_time:
      RPL.servoWrite(0,
