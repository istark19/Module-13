import RoboPiLib as RPL
import setup
import time

current_time = time.time()

while True:
  while int(current_time) % 3 != 0:
    import RoboPiLib as RPL
    import setup
    RPL.servoWrite(1,500)
    RPL.servoWrite(0,2000)
  
  while int(current_time) % 3 == 0:
    import RoboPiLib as RPL
    import setup
    RPL.servoWrite(1,0)
    RPL.servoWrite(0,0)
