import RoboPiLib as RPL
import setup
import time

current_time = time.time()

while True:
  while current_time % 3 != 0:
    import RoboPiLib as RPL
    import setup
    RPL.servoWrite(1,500)
    RPL.servoWrite(0,2000)
  
  while current_time % 3 == 0:
    import RoboPiLib as RPL
    import setup
    RPL.servoWrite(1,0)
    RPL.servoWrite(0,0)
