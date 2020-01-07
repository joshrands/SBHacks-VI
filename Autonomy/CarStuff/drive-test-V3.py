import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


class drive:
    def __init__(self, flf, flb, frf, frb, blf, blb, brf, brb):
        self.turnTime = 1
        self.FLF = flf
        self.FLB = flb
        self.FRF = frf
        self.FRB = frb
        self.BLF = blf
        self.BLB = blb
        self.BRF = brf
        self.BRB = brb
        self.LS = 7
        self.RS = 11
        self.leftCount = 0
        self.rightCount = 0

        GPIO.setup(self.FLF, GPIO.OUT)
        GPIO.setup(self.FLB, GPIO.OUT)
        GPIO.setup(self.FRF, GPIO.OUT)
        GPIO.setup(self.FRB, GPIO.OUT)
        GPIO.setup(self.BLF, GPIO.OUT)
        GPIO.setup(self.BLB, GPIO.OUT)
        GPIO.setup(self.BRF, GPIO.OUT)
        GPIO.setup(self.BRB, GPIO.OUT)

        GPIO.setup(self.LS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.RS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(self.LS, GPIO.FALLING, callback = self.leftIterate, bouncetime = 10)
        GPIO.add_event_detect(self.RS, GPIO.FALLING, callback = self.rightIterate, bouncetime = 10)
        
        self.FLF_PWM = GPIO.PWM(self.FLF, 1000)
        self.FLB_PWM = GPIO.PWM(self.FLB, 1000)
        self.FRF_PWM = GPIO.PWM(self.FRF, 1000)
        self.FRB_PWM = GPIO.PWM(self.FRB, 1000)
        self.BLF_PWM = GPIO.PWM(self.BLF, 1000)
        self.BLB_PWM = GPIO.PWM(self.BLB, 1000)
        self.BRF_PWM = GPIO.PWM(self.BRF, 1000)
        self.BRB_PWM = GPIO.PWM(self.BRB, 1000)

        self.FLF_PWM.start(0)
        self.FLB_PWM.start(0)
        self.FRF_PWM.start(0)
        self.FRB_PWM.start(0)
        self.BLF_PWM.start(0)
        self.BLB_PWM.start(0)
        self.BRF_PWM.start(0)
        self.BRB_PWM.start(0)

    def end(self):
        self.FLF_PWM.stop()
        self.FLB_PWM.stop()
        self.FRF_PWM.stop()
        self.FRB_PWM.stop()
        self.BLF_PWM.stop()
        self.BLB_PWM.stop()
        self.BRF_PWM.stop()
        self.BRB_PWM.stop()

    def stop(self):
        self.FLF_PWM.ChangeDutyCycle(0)
        self.FLB_PWM.ChangeDutyCycle(0)
        self.FRF_PWM.ChangeDutyCycle(0)
        self.FRB_PWM.ChangeDutyCycle(0)
        self.BLF_PWM.ChangeDutyCycle(0)
        self.BLB_PWM.ChangeDutyCycle(0)
        self.BRF_PWM.ChangeDutyCycle(0)
        self.BRB_PWM.ChangeDutyCycle(0)

    def forward(self, duty_cycle):
        self.FLF_PWM.ChangeDutyCycle(duty_cycle)
        self.FLB_PWM.ChangeDutyCycle(0)
        self.FRF_PWM.ChangeDutyCycle(duty_cycle)
        self.FRB_PWM.ChangeDutyCycle(0)
        self.BLF_PWM.ChangeDutyCycle(duty_cycle)
        self.BLB_PWM.ChangeDutyCycle(0)
        self.BRF_PWM.ChangeDutyCycle(duty_cycle)
        self.BRB_PWM.ChangeDutyCycle(0)

    def backward(self, duty_cycle):
        self.FLF_PWM.ChangeDutyCycle(0)
        self.FLB_PWM.ChangeDutyCycle(duty_cycle)
        self.FRF_PWM.ChangeDutyCycle(0)
        self.FRB_PWM.ChangeDutyCycle(duty_cycle)
        self.BLF_PWM.ChangeDutyCycle(0)
        self.BLB_PWM.ChangeDutyCycle(duty_cycle)
        self.BRF_PWM.ChangeDutyCycle(0)
        self.BRB_PWM.ChangeDutyCycle(duty_cycle)

    def left_turn(self):
        self.FLF_PWM.ChangeDutyCycle(0)
        self.FLB_PWM.ChangeDutyCycle(100)
        self.FRF_PWM.ChangeDutyCycle(100)
        self.FRB_PWM.ChangeDutyCycle(0)
        self.BLF_PWM.ChangeDutyCycle(0)
        self.BLB_PWM.ChangeDutyCycle(100)
        self.BRF_PWM.ChangeDutyCycle(100)
        self.BRB_PWM.ChangeDutyCycle(0)
        time.sleep(self.turnTime)

    def right_turn(self):
        self.FLF_PWM.ChangeDutyCycle(100)
        self.FLB_PWM.ChangeDutyCycle(0)
        self.FRF_PWM.ChangeDutyCycle(0)
        self.FRB_PWM.ChangeDutyCycle(100)
        self.BLF_PWM.ChangeDutyCycle(100)
        self.BLB_PWM.ChangeDutyCycle(0)
        self.BRF_PWM.ChangeDutyCycle(0)
        self.BRB_PWM.ChangeDutyCycle(100)
        time.sleep(self.turnTime)

    def leftIterate(self, channel):
        self.leftCount = self.leftCount + 1
        print("Left Count: ", self.leftCount, "\n")

    def rightIterate(self, channel):
        self.rightCount = self.rightCount + 1
        print("Right Count: ", self.rightCount, "\n")


car = drive(37, 35, 31, 33, 40, 38, 16, 18)

car.forward(100)
time.sleep(5)
car.stop()
'''
car.backward(100)
time.sleep(1)
car.stop()
car.left_turn(100)
time.sleep(1)
car.stop()
car.right_turn(100)
time.sleep(1)
car.stop()
'''
