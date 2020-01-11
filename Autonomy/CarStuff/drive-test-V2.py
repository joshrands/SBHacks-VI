import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class drive:
    def __init__(self, flf, flb, frf, frb, blf, blb, brf, brb):
        self.FLF = flf
        self.FLB = flb
        self.FRF = frf
        self.FRB = frb
        self.BLF = blf
        self.BLB = blb
        self.BRF = brf
        self.BRB = brb

        GPIO.setup(self.FLF, GPIO.OUT)
        GPIO.setup(self.FLB, GPIO.OUT)
        GPIO.setup(self.FRF, GPIO.OUT)
        GPIO.setup(self.FRB, GPIO.OUT)
        GPIO.setup(self.BLF, GPIO.OUT)
        GPIO.setup(self.BLB, GPIO.OUT)
        GPIO.setup(self.BRF, GPIO.OUT)
        GPIO.setup(self.BRB, GPIO.OUT)

        self.FLF_PWM = GPIO.PWM(self.FLF,1000)
        self.FLB_PWM = GPIO.PWM(self.FLB,1000)
        self.FRF_PWM = GPIO.PWM(self.FRF,1000)
        self.FRB_PWM = GPIO.PWM(self.FRB,1000)
        self.BLF_PWM = GPIO.PWM(self.BLF,1000)
        self.BLB_PWM = GPIO.PWM(self.BLB,1000)
        self.BRF_PWM = GPIO.PWM(self.BRF,1000)
        self.BRB_PWM = GPIO.PWM(self.BRB,1000)

        self.FLF_PWM.start(0)
        self.FLB_PWM.start(0)
        self.FRF_PWM.start(0)
        self.FRB_PWM.start(0)
        self.BLF_PWM.start(0)
        self.BLB_PWM.start(0)
        self.BRF_PWM.start(0)
        self.BRB_PWM.start(0)

    def stop(self):
        self.FLF_PWM.ChangeDutyCycle(0)
        self.FLB_PWM.ChangeDutyCycle(0)
        self.FRF_PWM.ChangeDutyCycle(0)
        self.FRB_PWM.ChangeDutyCycle(0)
        self.BLF_PWM.ChangeDutyCycle(0)
        self.BLB_PWM.ChangeDutyCycle(0)
        self.BRF_PWM.ChangeDutyCycle(0)
        self.BRB_PWM.ChangeDutyCycle(0)

    def forward(self,duty_cycle):
        self.FLF_PWM.ChangeDutyCycle(duty_cycle)
        self.FLB_PWM.ChangeDutyCycle(duty_cycle)
        self.FRF_PWM.ChangeDutyCycle(duty_cycle)
        self.FRB_PWM.ChangeDutyCycle(duty_cycle)
        self.BLF_PWM.ChangeDutyCycle(duty_cycle)
        self.BLB_PWM.ChangeDutyCycle(duty_cycle)
        self.BRF_PWM.ChangeDutyCycle(duty_cycle)
        self.BRB_PWM.ChangeDutyCycle(duty_cycle)


car = drive(18,16,38,40,33,31,35,37)
car.forward(50)
time.sleep(2)
car.stop()