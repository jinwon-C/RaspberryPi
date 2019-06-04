import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        if GPIO.input(25):
            print("on")
            GPIO.output(24, 1)
        else:
            print("off")
            GPIO.output(24, 0)
        sleep(0.2)
finally:
    GPIO.cleanup()
