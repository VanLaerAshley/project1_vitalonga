import RPi.GPIO as GPIO
import time

class Servo:

    def __init__(self):
        pass


def aanzetten(start):
    aanUitMotor = 13
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(aanUitMotor, GPIO.OUT)
    onOf = GPIO.PWM(aanUitMotor, 50)
    onOf.start(7)
    if (start == "aan") or (start == "uit"):
        onOf.ChangeDutyCycle(3)
        time.sleep(1)
        onOf.ChangeDutyCycle(7)
        time.sleep(1)
    onOf.stop()
    GPIO.cleanup()


def keuzeMaken(keuze):
    motor = 12
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor, GPIO.OUT)
    p = GPIO.PWM(motor, 50)
    p.start(7)
    if keuze == "espresso":
        p.ChangeDutyCycle(5.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7)
        time.sleep(1)
        p.stop()
    if keuze == "lungo":
        p.ChangeDutyCycle(9)
        time.sleep(0.5)
        p.ChangeDutyCycle(7)
        time.sleep(1)
        p.stop()
    GPIO.cleanup()


#Volume wijzigen
def volume(keuze):
    motor = 12
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor, GPIO.OUT)
    p = GPIO.PWM(motor, 50)
    p.start(7)
    if keuze == "espresso":
        p.ChangeDutyCycle(5.5)
        time.sleep()
    if keuze == "lungo":
        p.ChangeDutyCycle(9)
        time.sleep(1)
    if keuze == "einde":
        p.ChangeDutyCycle(7)
        time.sleep(1)
        p.stop()
    GPIO.cleanup()






