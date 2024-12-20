import RPi.GPIO as GPIO
import serial

led=40

uart_channel= serial.Serial("/dev/ttyS0", baudrate=9600, timeout=2)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
# servo1 = GPIO.PWM(40,50)
# GPIO.setwarnings(False)

while True:
    try:
              
        data = uart_channel.read()
        receive = str(data)
        print(receive)
            
        if(receive == "1"):
            GPIO.output(led, GPIO.HIGH)
            print("LED on")
#             for angle in range(0,180,10):
#                 servo1.ChangeDutyCycle(2+(angle/18))
            
                
        elif(receive == "0"):
            GPIO.output(led,GPIO.LOW)
#                 for duty in range(180,0,-10):
#                     servo1.ChangeDutyCycle(2+(angle/18))
#     
    except KeyboardInterrupt:
        print("\nProgram ended")
        break

GPIO.cleanup()
                
                
                