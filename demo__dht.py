import Adafruit_DHT

while True:
    humidity,temerature = Adafruit_DHT.read(Adafruit_DHT.DHT11,23)
    print('Temp={0.01f}C Humidity={0.01f%}'.format(temperatue,humidity))