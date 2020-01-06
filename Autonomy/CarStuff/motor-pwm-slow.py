import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

# simulate pwm! 
for i in range(0, 100):
    GPIO.output(7, True)
    time.sleep(0.01)
    GPIO.output(7, False)
    time.sleep(0.03)


GPIO.cleanup()

