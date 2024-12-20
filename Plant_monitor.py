import RPi.GPIO as GPIO
#import Adafruit_DHT
import time
#import rplcd

# GPIO Pin configuration
SOIL_MOISTURE_PIN = 26
#DHT_PIN = 4
RELAY_PIN = 20
BUZZER_PIN = 21

# I2C LCD Configuration
#I2C_ADDRESS = 0x27  # Replace with your LCD's I2C address
#lcd = CharLCD('PCF8574', I2C_ADDRESS)

# Threshold values
MOISTURE_THRESHOLD = 600  # Adjust based on sensor calibration
TEMP_THRESHOLD = 35  # Temperature in °C
HUMIDITY_THRESHOLD = 30  # Humidity in %

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Initialize outputs
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure pump is off initially
GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure buzzer is off initially

# Function to read soil moisture
def read_soil_moisture():
    return GPIO.input(SOIL_MOISTURE_PIN)

# Function to read temperature and humidity
#def read_dht_sensor():
#    sensor = Adafruit_DHT.DHT11
#    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
#    return humidity, temperature

# Function to activate the buzzer
def activate_buzzer(duration):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Function to update LCD
#def update_lcd(message):
#    lcd.clear()
#    lcd.write_string(message)

# Main loop
try:
    while True:
        soil_moisture = read_soil_moisture()
#        humidity, temperature = read_dht_sensor()
       # Determine soil status
                  
#        print(f"Soil: {soil_status}, Temp: {temperature}°C, Humidity: {humidity}%")
               
        # Update LCD display
#        lcd_message = f"Soil: {soil_status}\nTemp: {temperature}C Hum:{humidity}%"
#        update_lcd(lcd_message)
       
        # Compare values and control the pump
#        if soil_moisture == 0 and temperature < TEMP_THRESHOLD and humidity < HUMIDITY_THRESHOLD:
        if GPIO.input(SOIL_MOISTURE_PIN):
            soil_status = "Dry"
            print(f"Soil: {soil_status}")

            print("Activating pump...")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn pump ON
            activate_buzzer(1)  # Buzzer sound for 1 second
#            update_lcd("Pump: ON\nWatering soil...")
            time.sleep(5)  # Pump water for 5 seconds
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn pump OFF
        else:
            soil_status = "Wet"
            print(f"Soil: {soil_status}")
            print("Conditions not met. Pump is OFF.")
                   
        time.sleep(10)  # Wait 10 seconds before next check

except KeyboardInterrupt:
    print("Exiting program...")
finally:
#    lcd.clear()
    GPIO.cleanup()