import RPi.GPIO as GPIO
import requests
import time
import random

TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)

while 1:
    print("Sending data to ThingSpeak")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    time.sleep(2)

    URL= "https://api.thingspeak.com/update?api_key=K3FTT2NF6G5CNWA8&field1=" + str(distance)
    r=requests.get(URL)
    print(r)
    time.sleep(15)