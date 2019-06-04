import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)

count = 0
pwm = GPIO.PWM(16, 50)
pwm.start(0)

try:
    while True:
        input_state = GPIO.input(12)
        if input_state == False:
            count += 1
            print(str(count)+ ' pressed')
            time.sleep(0.2)
        if count%4 == 0:
            pwm.ChangeDutyCycle(25)
        elif count%4 == 1:
            pwm.ChangeDutyCycle(50)
        elif count%4 == 2:
            pwm.ChangeDutyCycle(75)
        else:
            pwm.ChangeDutyCycle(100)
except KeyboardInterrupt():
    GPIO.cleanup()


