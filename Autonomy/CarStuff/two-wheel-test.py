# script to test driving! 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LEFT_FORWARD = 18
LEFT_BACKWARD = 16
RIGHT_FORWARD = 38
RIGHT_BACKWARD = 40

GPIO.setup(LEFT_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_BACKWARD, GPIO.OUT)
GPIO.setup(RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_BACKWARD, GPIO.OUT)

def drive_wheel(duration, PIN):
    for i in range(0, duration*25):
        GPIO.output(PIN, True)
        time.sleep(0.01)
        GPIO.output(PIN, False)
        time.sleep(0.03)

# Move left wheel forward, then back 
drive_wheel(1, LEFT_FORWARD)
drive_wheel(1, LEFT_BACKWARD)
# same with right 
drive_wheel(1, RIGHT_FORWARD)
drive_wheel(1, RIGHT_BACKWARD)

GPIO.cleanup()

