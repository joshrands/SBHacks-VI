# script to test driving! 

import RPi.GPIO as GPIO
import time
import random 

from drive import *
from distance import *

GPIO.setmode(GPIO.BOARD)
back_wheels = TwoWheel(18, 16, 38, 40)
front_wheels = TwoWheel(33, 31, 35, 37)

# Make car 
drive = FourWheel(front_wheels, back_wheels)
drive.stop()

# Make sonar sensor 
sonar = UltraSonic(15, 13)

# end this program by putting hand on sonar sensor! 
while (sonar.get_distance() == -1 or sonar.get_distance() > 7):
    
    # is there an obstacle? 
    if (sonar.get_distance() != -1 and sonar.get_distance() < 20):

        # confirm data
        obstacle = True
        for i in range(0, 2):
            if (sonar.get_distance() == -1 or sonar.get_distance() >= 20):
                obstacle = False
            time.sleep(0.05)

        if (obstacle):
            print("Obstacle detected! Turning left...")

            # backup first
            drive.drive_backward(1)

            direction = random.randint(0,1)
            if (direction == 0):
                drive.pivot_left(0.5)
            else:
                drive.pivot_right(0.5)

    print("Driving forward...")
    drive.drive_forward(0.5)

print("All done!")
drive.stop()

GPIO.cleanup()

