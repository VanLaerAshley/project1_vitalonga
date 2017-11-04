# Import required libraries
import time
import sys
import RPi.GPIO as GPIO

class StepperHall:
    def __init__(self, stepperPins, hallPin):
        self.__stepperPins = stepperPins
        self.__hallPin = hallPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(hallPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(hallPin, GPIO.BOTH, bouncetime=200)

    def steps(self):
        for pin in self.__stepperPins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        self.Seq = [[1, 0, 0, 1],
                   [1, 0, 0, 0],
                   [1, 1, 0, 0],
                   [0, 1, 0, 0],
                   [0, 1, 1, 0],
                   [0, 0, 1, 0],
                   [0, 0, 1, 1],
                   [0, 0, 0, 1]]

    def waitTime(self):
        if len(sys.argv) > 1:
            self.WaitTime = int(sys.argv[1]) / float(10000)
        else:
            self.WaitTime = 10 / float(10000)
        self.StepCount = len(self.Seq)
        self.StepCounter = 0
        self.StepDir = 1

    def stepperToHall(self):
        while GPIO.input(self.__hallPin) == True:
            if GPIO.input(self.__hallPin) == True:
                # no magnet motor runs
                print("Sensor HIGH ")
                for pin in range(0, 4):
                    xpin = self.__stepperPins[pin]  # Get GPIO
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                self.StepCounter += self.StepDir

                # If we reach the end of the sequence
                # start again
                if (self.StepCounter >= self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter < 0):
                    self.StepCounter = self.StepCount + self.StepDir
                # Wacht voor bewegen
                time.sleep(self.WaitTime)
            if GPIO.input(self.__hallPin) == False:
                # Magnet motor stops
                print("Sensor LOW ")

    def keuzeKoffie(self, capsulenaam):
        if capsulenaam == "1":
            self.loop = 0
            for self.loop in range(0, 20):
                print("anti-clockwise")
                self.StepDir = 1
                for pin in range(0, 4):
                    xpin = self.__stepperPins[pin]  # Get GPIO
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                self.StepCounter += self.StepDir
                self.loop += 1
                # If we reach the end of the sequence
                # start again
                if (self.StepCounter >= self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter < 0):
                    self.StepCounter = self.StepCount + self.StepDir
                # Wait before moving on
                time.sleep(self.WaitTime)

        if capsulenaam == "2":
            self.loop = 0
            for self.loop in range(0, 1050):
                print("anti-clockwise")
                self.StepDir = 1
                for pin in range(0, 4):
                    xpin = self.__stepperPins[pin]  # Get GPIO
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                self.StepCounter += self.StepDir
                self.loop += 1
                # If we reach the end of the sequence
                # start again
                if (self.StepCounter >= self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter < 0):
                    self.StepCounter = self.StepCount + self.StepDir
                # Wait before moving on
                time.sleep(self.WaitTime)

        if capsulenaam == "3":
            self.loop = 0
            for self.loop in range(0, 2080):
                print("anti-clockwise")
                self.StepDir = 1
                for pin in range(0, 4):
                    xpin = self.__stepperPins[pin]  # Get GPIO
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                self.StepCounter += self.StepDir
                self.loop += 1
                # If we reach the end of the sequence
                # start again
                if (self.StepCounter >= self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter < 0):
                    self.StepCounter = self.StepCount + self.StepDir
                # Wait before moving on
                time.sleep(self.WaitTime)

        if capsulenaam == "4":
            self.loop = 0
            for self.loop in range(0, 3095):
                print("anti-clockwise")
                self.StepDir = 1
                for pin in range(0, 4):
                    xpin = self.__stepperPins[pin]  # Get GPIO
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                self.StepCounter += self.StepDir
                self.loop += 1
                # If we reach the end of the sequence
                # start again
                if (self.StepCounter >= self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter < 0):
                    self.StepCounter = self.StepCount + self.StepDir
                # Wait before moving on
                time.sleep(self.WaitTime)

        if capsulenaam == "5":
            self.loop = 0
            for self.loop in range(0, 600):
                print("anti-clockwise")
                self.StepDir = 1
                for pin in range(0, 4):
                    xpin = self.__stepperPins[pin]  # Get GPIO
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)
                self.StepCounter += self.StepDir
                self.loop += 1
                # If we reach the end of the sequence
                # start again
                if (self.StepCounter >= self.StepCount):
                    self.StepCounter = 0
                if (self.StepCounter < 0):
                    self.StepCounter = self.StepCount + self.StepDir
                # Wait before moving on
                time.sleep(self.WaitTime)
        return capsulenaam

    GPIO.cleanup()

