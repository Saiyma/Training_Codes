import requests
import time
import random

while 1:
    print("Sending data to ThingSpeak")
    data= random.randint(0,200)
    URL= "https://api.thingspeak.com/update?api_key=K3FTT2NF6G5CNWA8&field1=" + str(data)
    r=requests.get(URL)
    print(r)
    time.sleep(15)