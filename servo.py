import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

servo1 = GPIO.PWM(7,50) #pin, Frequency
servo1.start(7.5)

try:
	while True:
		servo1.ChangeDutyCycle(7.5) #Neutral
		time.sleep(1)
		servo1.ChangeDutyCycle(12.5) #180 degrees
		time.sleep(1)
		servo1.ChangeDutyCycle(7.5) #0 degrees
		time.sleep(1)
except KeyboardInterrupt:
	servo1.stop()
	GPIO.cleanup()

