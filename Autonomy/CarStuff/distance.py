
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class UltraSonic:

    def __init__(self, trigger, echo):
        self.TRIGGER = trigger
        self.ECHO = echo

        GPIO.setup(self.TRIGGER, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def get_distance(self):
        # set trigger to HIGH
        GPIO.output(self.TRIGGER, True)

        time.sleep(0.00001) # 0.01ms to LOW
        GPIO.output(self.TRIGGER, False)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.ECHO) == 0:
            start_time = time.time()

        while GPIO.input(self.ECHO) == 1:
            stop_time = time.time()

        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2

        if (distance > 400):
            distance = -1

        return distance


#GPIO_TRIGGER = 22
#GPIO_ECHO = 27

#sonar = UltraSonic(GPIO_TRIGGER, GPIO_ECHO)

#while True:
#    dist = sonar.get_distance()
#    print("Measured Distance = %.1f cm" % dist)
#    time.sleep(0.2)


