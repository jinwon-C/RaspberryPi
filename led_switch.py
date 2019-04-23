import RPi.GPIO as GPIO
import time

led = 16
switch = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_UP)

count = 0
while True:
	input_state = GPIO.input(switch)
	if input_state == False:
		count += 1
		time.sleep(0.2)
	if count%2 == 0
		GPIO.output(led, True)
	else:
		GPIO.output(led, False)
