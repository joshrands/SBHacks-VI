import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

leftSensorPin = 7
rightSensorPin = 11

GPIO.setup(leftSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightSensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

left_sensor_state = 0
left_last_state = 0


right_sensor_state = 0
right_last_state = 0

try:
    while True:
        left_sensor_state = GPIO.input(leftSensorPin)
        if left_sensor_state:
            print('left connected')

        if not left_sensor_state:
            print('left broken')

        left_last_state = left_sensor_state

        right_sensor_state = GPIO.input(rightSensorPin)
        if right_sensor_state:
            print('right connected')

        if not right_sensor_state:
            print('right broken')

        right_last_state = right_sensor_state

        time.sleep(1)

finally:
    GPIO.cleanup()
