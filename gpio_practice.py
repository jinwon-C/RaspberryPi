import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)

count = 3
pwm = GPIO.PWM(16, 50)
pwm.start(0)

try:
    while True:
        input_state = GPIO.input(20)
        if count%4 == 0:
            pwm.ChangeDutyCycle(25)
            if input_state == False:
                count += 1
                print(str(count)+ ' pressed')
                break
        elif count%4 == 1:
            pwm.ChangeDutyCycle(50)
            if input_state == False:
                count += 1
                print(str(count)+ ' pressed')
                break
        elif count%4 == 2:
            pwm.ChangeDutyCycle(75)
            if input_state == False:
                count += 1
                print(str(count)+ ' pressed')
                break
        else:
            pwm.ChangeDutyCycle(100)
            if input_state == False:
                count += 1
                print(str(count)+ ' pressed')
                break
except KeyboardInterrupt():
    GPIO.cleanup()


