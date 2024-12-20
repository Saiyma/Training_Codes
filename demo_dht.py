import RPi.GPIO as GPIO
import sys 
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.DHT11, 23)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

