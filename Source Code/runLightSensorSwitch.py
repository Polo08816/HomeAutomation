import RPi.GPIO as GPIO
import time

import sys

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


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
        
    time.sleep(0.8)
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
            print("Turn on switch.")
            response = urllib2.urlopen('http://localhost:8083/ZWaveAPI/Run/devices[2].instances[0].commandClasses[0x25].Set(255)')
            # html = response.read()
            # print(html)
        else:
            print("LED Off!")
            GPIO.output(ledPin, GPIO.LOW)
            print("Turn off switch.")
            response = urllib2.urlopen('http://localhost:8083/ZWaveAPI/Run/devices[2].instances[0].commandClasses[0x25].Set(0)')
            # html = response.read()
            # print(html)
        
        
GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup()