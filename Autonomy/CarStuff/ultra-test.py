import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trigPin = 8
echoPin = 10

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def distUltra():
    GPIO.output(trigPin, True)

    time.sleep(0.00001)
    GPIO.output(trigPin, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(echoPin) == 0:
        StartTime = time.time()

    while GPIO.input(echoPin) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

while True:
    dist1 = distUltra()
    print(dist1)
    time.sleep(.25)
