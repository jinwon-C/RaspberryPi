import RPi.GPIO as GPIO
import time

pin = 12

GPIO.setmode(GPIO.BCM)
#GPIO.setup(pin, GPIO.IN)
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

count = 0

try:
    while True:
        input_state = GPIO.input(pin)
        if input_state == True:
            count += 1
            print (str(count) + ' pressed')
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()


