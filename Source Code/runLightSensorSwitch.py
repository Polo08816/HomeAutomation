import RPi.GPIO as GPIO
import time

import sys

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
import array
    
import numpy as np
import pandas as pd


# pin definitions for outputs
ledPin = 22

# pin definitions for inputs
lightSensorPin = 4

# light reading threshold
lightActivationThreshold = 800

# set rolling Average Light Reading to activation threshold
rollingAverageLightReading = lightActivationThreshold


# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setwarnings(False)


# light dependent sensor
print("Light Sensor!")

#default light sensor reading
lightReading = 0

# set up array for rolling averages

lightReadingArray = np.array([lightActivationThreshold, lightActivationThreshold, lightActivationThreshold, lightActivationThreshold, lightActivationThreshold])
# lightReadingArray = {'light': [lightActivationThreshold, lightActivationThreshold, lightActivationThreshold, lightActivationThreshold, lightActivationThreshold]}

# print(lightReadingArray)

df = pd.DataFrame(lightReadingArray)

# print(df)




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
        
        # add current light reading to array

        df = df.append([lightReading], ignore_index = True) #adding to the end
        df = df.iloc[1:] # drop first row
        
        # print(df)
        
        print('')
        rollingAverageLightReading = df[0].mean()
        print('Rolling Average: ', rollingAverageLightReading)
        print('')
        
        
        if (rollingAverageLightReading < 800):
            print("LED On!")
            GPIO.output(ledPin, GPIO.HIGH)
            print("Turn on switch.")
            response = urllib2.urlopen('http://localhost:8083/ZWaveAPI/Run/devices[2].instances[0].commandClasses[0x25].Set(255)')
            html = response.read()
            # print(html)
        else:
            print("LED Off!")
            GPIO.output(ledPin, GPIO.LOW)
            print("Turn off switch.")
            response = urllib2.urlopen('http://localhost:8083/ZWaveAPI/Run/devices[2].instances[0].commandClasses[0x25].Set(0)')
            html = response.read()
            # print(html)
        
        
GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup()