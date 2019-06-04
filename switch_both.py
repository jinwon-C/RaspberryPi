import RPi.GPIO as GPIO
import datetime

def my_callback(channel):
    if GPIO.input(6) == GPIO.HIGH:
        print('HIGH ' +str(datetime.datetime.now()))
    else:
        print('LOW ' +str(datetime.datetime.now()))

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)

    message = raw_input('exit')
finally:
    GPIO.cleanup()
