#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
while True:
        if GPIO.input(channel):
                print("No Water Detected!")
        else:
                print("Water Detected!")

        time.sleep(2)
 

 
