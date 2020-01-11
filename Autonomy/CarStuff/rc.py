# script to test driving! 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class TwoWheel:
    def __init__(self, left_for, left_back, right_for, right_back):
        self.LEFT_FORWARD = left_for
        self.LEFT_BACKWARD = left_back
        self.RIGHT_FORWARD = right_for
        self.RIGHT_BACKWARD = right_back

        GPIO.setup(self.LEFT_FORWARD, GPIO.OUT)
        GPIO.setup(self.LEFT_BACKWARD, GPIO.OUT)
        GPIO.setup(self.RIGHT_FORWARD, GPIO.OUT)
        GPIO.setup(self.RIGHT_BACKWARD, GPIO.OUT)

    def stop(self):
        GPIO.output(self.LEFT_FORWARD, False)
        GPIO.output(self.LEFT_BACKWARD, False)
        GPIO.output(self.RIGHT_FORWARD, False)
        GPIO.output(self.RIGHT_BACKWARD, False)

    def drive_forward(self):
        GPIO.output(self.LEFT_FORWARD, True)
        GPIO.output(self.RIGHT_FORWARD, True)

    def drive_backward(self):
        GPIO.output(self.LEFT_BACKWARD, True)
        GPIO.output(self.RIGHT_BACKWARD, True)

    def pivot_left(self):
        GPIO.output(self.RIGHT_FORWARD, True)
        GPIO.output(self.RIGHT_BACKWARD, False)
        GPIO.output(self.LEFT_BACKWARD, True)
        GPIO.output(self.LEFT_FORWARD, False)

    def pivot_right(self):
        GPIO.output(self.RIGHT_FORWARD, False)
        GPIO.output(self.RIGHT_BACKWARD, True)
        GPIO.output(self.LEFT_BACKWARD, False)
        GPIO.output(self.LEFT_FORWARD, True)

class FourWheel:
    def __init__(self, front, back):
        self.front_wheels = front
        self.back_wheels = back

        self.front_wheels.stop()
        self.back_wheels.stop()

    def drive_forward(self, duration, speed=25):
        end = int(duration*25.0)
        for i in range(0, end): 
            self.front_wheels.drive_forward()
            self.back_wheels.drive_forward()
            time.sleep(.04 * (speed/100.0))
            self.stop()
            time.sleep(0.04 * (speed/100.0) * 3)

    def drive_backward(self, duration, speed=25):
        end = int(duration*25.0)
        for i in range(0, end): 
            self.front_wheels.drive_backward()
            self.back_wheels.drive_backward()
            time.sleep(.04 * (speed/100.0))
            self.stop()
            time.sleep(0.04 * (speed/100.0) * 3)

    def pivot_left(self, duration):
        self.front_wheels.pivot_left()
        self.back_wheels.pivot_left()
        time.sleep(duration)
        self.stop()

    def pivot_right(self, duration):
        self.front_wheels.pivot_right()
        self.back_wheels.pivot_right()
        time.sleep(duration)
        self.stop()

    def stop(self):
        self.front_wheels.stop()
        self.back_wheels.stop()

back_wheels = TwoWheel(18, 16, 38, 40)
front_wheels = TwoWheel(33, 31, 35, 37)

drive = FourWheel(front_wheels, back_wheels)
drive.stop()

op = "s"
while (op != "q"):
    op = input(":")
    print(op)
    op = str(op)

    if (op == "a"):
        drive.pivot_left(0.25)
    elif (op == "s"):
        drive.drive_backward(1)
    elif (op == "d"):
        drive.pivot_right(0.25)
    elif (op == "w"):
        drive.drive_forward(1)
    elif (op == "q"):
        print("Ending RC")
    else:
        print("Unknown command")

drive.stop()

GPIO.cleanup()

