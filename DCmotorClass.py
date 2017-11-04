from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit
import RPi.GPIO as GPIO

class OpenCapsuleTray:
    def __init__(self, sluisBeneden, sluisBoven):
        self.__i2cAdrr = Adafruit_MotorHAT(addr=0x60)
        self.__sluisBeneden = sluisBeneden
        self.__sluisBoven = sluisBoven
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sluisBeneden, GPIO.OUT)
        GPIO.setup(sluisBoven, GPIO.OUT)
        self.beneden = GPIO.PWM(sluisBeneden, 50)
        self.boven = GPIO.PWM(sluisBoven, 50)

    def turnOffMotors(self):
        self.__i2cAdrr.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.__i2cAdrr.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.__i2cAdrr.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.__i2cAdrr.getMotor(4).run(Adafruit_MotorHAT.RELEASE)



    def runSequence(self):
        atexit.register(self.turnOffMotors)
        self.myMotor = self.__i2cAdrr.getMotor(3)

        self.myMotor.run(Adafruit_MotorHAT.FORWARD)
        print("open")
        self.myMotor.setSpeed(155)
        time.sleep(0.1)
        self.myMotor.setSpeed(40)
        time.sleep(3)

        print("Release")
        self.myMotor.run(Adafruit_MotorHAT.RELEASE)
        time.sleep(0.2)

        self.beneden.start(9.5)
        self.boven.start(5)


        self.boven.ChangeDutyCycle(8.5)
        time.sleep(1)
        self.beneden.ChangeDutyCycle(5.5)
        time.sleep(3)
        self.beneden.ChangeDutyCycle(2)
        time.sleep(1)
        self.beneden.ChangeDutyCycle(9.5)
        time.sleep(1)
        self.boven.ChangeDutyCycle(5)
        time.sleep(1)
        self.beneden.stop()
        self.boven.stop()

        self.myMotor.run(Adafruit_MotorHAT.BACKWARD)
        print("toe")
        self.myMotor.setSpeed(70)
        time.sleep(3)
        self.myMotor.setSpeed(155)
        time.sleep(0.4)
        print("Release")
        self.myMotor.run(Adafruit_MotorHAT.RELEASE)
        time.sleep(0.2)
        GPIO.cleanup()

    def servoAirOpen(self):
        self.beneden.start(9.5)
        self.beneden.ChangeDutyCycle(2)
        time.sleep(1)
        self.beneden.stop()
        GPIO.cleanup()

    def servoAirClose(self):
        self.beneden.start(2.5)
        self.beneden.ChangeDutyCycle(9.5)
        time.sleep(1)
        self.beneden.stop()
        GPIO.cleanup()


