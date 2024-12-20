import RPi.GPIO as GPIO
import time

# GPIO Pin configuration
RELAY_PIN = 27
BUZZER_PIN = 22

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Initialize outputs
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure pump is off initially
GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure buzzer is off initially

# Function to activate the buzzer
def activate_buzzer(duration):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Main loop
try:
    while True:
        usr_ip = str(input("Enter to turn on or off motor: "))
        if usr_ip == 'y':
            print("Activating pump...")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn pump ON
            activate_buzzer(1)  # Buzzer sound for 1 second
            time.sleep(5)  # Pump water for 5 seconds
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn pump OFF
        else:
            print("Conditions not met. Pump is OFF.")
            
        time.sleep(10)  # Wait 10 seconds before next check

except KeyboardInterrupt:
    print("Exiting program...")
finally:
    GPIO.cleanup()