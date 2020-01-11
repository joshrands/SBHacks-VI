import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

leftSensorPin = 7
rightSensorPin = 11

leftCount = 0
rightCount = 0

GPIO.setup(leftSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def leftIterate():
    leftCount += 1
    print("Left Count: ", leftCount, "\n")

def rightIterate():
    rightCount+= 1
    print("Right Count: ", rightCount, "\n")

GPIO.add_event_detect(leftSensorPin, GPIO.FALLING, leftIt = leftIterate(), bouncetime = 300)
GPIO.add_event_detect(rightSensorPin, GPIO.FALLING, rightIt = rightIterate(), bouncetime = 300)

try:
    print("Waiting for encoder moves..")
    time.sleep(2)

