import RPi.GPIO as GPIO
import time


#pin definitions for light LED
ledPin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledPin, GPIO.OUT) 

print("LED On!")

GPIO.output(ledPin, GPIO.HIGH)
time.sleep(6)

print("LED Off!")
GPIO.output(ledPin, GPIO.LOW)

GPIO.cleanup()