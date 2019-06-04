import RPi.GPIO as GPIO
import time

led = 16
freq = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, freq)
pwm.start(0)

try:
    while True:
        for dc in range(0, 100, 1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, 0, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
