import requests
import time
import RPi.GPIO as GPIO
import json

led = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)

while 1:
    URL = 'https://api.thingspeak.com/channels/2789789/fields/3.json?api_key=IDC8QRK29PX5G1FC&results=2'
    data = requests.get(URL).json()
    feeds_data= data['feeds']
    new_data=json.dumps(feeds_data)
    final_data=json.loads(new_data)
    
    for item in final_data:
        led_status=item['field3']
    if led_status == '1':
        print('Turn on LED')
        GPIO.output(led,GPIO.HIGH)
    else:
        print('Turn off LED')
        GPIO.output(led,GPIO.LOW)
        
    time.sleep(15)