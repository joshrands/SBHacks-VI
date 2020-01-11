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

        FLF_PWM = GPIO.PWM(self.FLF,1000)
        FLB_PWM = GPIO.PWM(self.FLB,1000)
        FRF_PWM = GPIO.PWM(self.FRF,1000)
        FRB_PWM = GPIO.PWM(self.FRB,1000)
        BLF_PWM = GPIO.PWM(self.BLF,1000)
        BLB_PWM = GPIO.PWM(self.BLB,1000)
        BRF_PWM = GPIO.PWM(self.BRF,1000)
        BRB_PWM = GPIO.PWM(self.BRB,1000)

        FLF_PWM.start(0)
        FLB_PWM.start(0)
        FRF_PWM.start(0)
        FRB_PWM.start(0)
        BLF_PWM.start(0)
        BLB_PWM.start(0)
        BRF_PWM.start(0)
        BRB_PWM.start(0)

    def stop(self):
        FLF_PWM.ChangeDutyCycle(0)
        FLB_PWM.ChangeDutyCycle(0)
        FRF_PWM.ChangeDutyCycle(0)
        FRB_PWM.ChangeDutyCycle(0)
        BLF_PWM.ChangeDutyCycle(0)
        BLB_PWM.ChangeDutyCycle(0)
        BRF_PWM.ChangeDutyCycle(0)
        BRB_PWM.ChangeDutyCycle(0)

    def forward(self,duty_cycle):
        FLF_PWM.ChangeDutyCycle(duty_cycle)
        FLB_PWM.ChangeDutyCycle(duty_cycle)
        FRF_PWM.ChangeDutyCycle(duty_cycle)
        FRB_PWM.ChangeDutyCycle(duty_cycle)
        BLF_PWM.ChangeDutyCycle(duty_cycle)
        BLB_PWM.ChangeDutyCycle(duty_cycle)
        BRF_PWM.ChangeDutyCycle(duty_cycle)
        BRB_PWM.ChangeDutyCycle(duty_cycle)


car = drive(18,16,38,40,33,31,35,37)
car.forward(50)
time.sleep(2)
car.stop()