import RPi.GPIO as GPIO
import time


#pin definitions for outputs
ledPin = 22

#pin definitions for inputs
lightSensorPin = 4

#setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setwarnings(False)


#light dependent sensor
print("Light Sensor!")


lightReading = 0

def RCtime (RCpin):
    reading = 0
        
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
        
    time.sleep(0.5)
    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading
    
while True:
        
        lightReading = RCtime(lightSensorPin)
        print(lightReading)
        if (lightReading < 800):
            print("LED On!")
            GPIO.output(ledPin, GPIO.HIGH)
        else:
            print("LED Off!")
            GPIO.output(ledPin, GPIO.LOW)
        
GPIO.cleanup()