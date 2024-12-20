import RPi.GPIO as GPIO
import time

# Pin configuration
SOIL_SENSOR_PIN = 26 
RELAY_PIN = 20       
BUZZER_PIN = 21       

# GPIO setup
GPIO.setmode(GPIO.BCM)       
GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)  
GPIO.setup(RELAY_PIN, GPIO.OUT)       
GPIO.setup(BUZZER_PIN, GPIO.OUT)      

# Initial state
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay off
GPIO.output(BUZZER_PIN, GPIO.LOW)

print("Automated Irrigation System Running. Press Ctrl+C to exit.")

try:
    while True:
        # Read soil moisture sensor
        soil_dry = GPIO.input(SOIL_SENSOR_PIN)  # HIGH if soil is dry, LOW if wet
        
        if soil_dry:  # Soil is dry
            print("Soil is dry. Turning on the pump.")
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Activate relay (turn on pump)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on buzzer for alert
        else:  # Soil is wet
            print("Soil is wet. Turning off the pump.")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Deactivate relay (turn off pump)
            GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off buzzer
        
        time.sleep(1)  # Wait for 1 second before next reading

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    # Cleanup GPIO states
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure relay is off
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure buzzer is off
    GPIO.cleanup()