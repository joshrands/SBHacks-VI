import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

leftSensorPin = 7
rightSensorPin = 11

leftCount = 0
rightCount = 0

GPIO.setup(leftSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def leftIterate(channel):
    global leftCount
    leftCount = leftCount + 1
    print("Left Count: ", leftCount, "\n")

def rightIterate(channel):
    global rightCount
    rightCount = rightCount + 1
    print("Right Count: ", rightCount, "\n")

GPIO.add_event_detect(leftSensorPin, GPIO.FALLING, callback = leftIterate, bouncetime = 300)
GPIO.add_event_detect(rightSensorPin, GPIO.FALLING, callback = rightIterate, bouncetime = 300)

while True:
    print("Waiting for encoder moves..")
    time.sleep(20)

