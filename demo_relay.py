import RPi.GPIO as GPIO
import time

# GPIO setup
RELAY_PIN = 14  # GPIO pin connected to the relay
BUZZER_PIN = 15  # GPIO pin connected to the buzzer

GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set relay pin as output
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set buzzer pin as output

# Initialize pins
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Ensure relay is off initially
GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure buzzer is off initially

def pump_on():
    """Turns the pump on and activates the buzzer."""
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Active LOW for most relays
    print("Pump ON")
    buzzer_beep()  # Sound alert for pump activation

def pump_off():
    """Turns the pump off and activates the buzzer."""
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Active LOW for most relays
    print("Pump OFF")
    buzzer_beep()  # Sound alert for pump deactivation

def buzzer_beep():
    """Activates the buzzer for a short duration."""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(0.5)  # Buzzer ON duration (0.5 seconds)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

try:
    print("Starting pump and buzzer control")
    while True:
        # Example sequence: Turn pump on for 5 seconds, then off for 5 seconds
        pump_on()
        time.sleep(2)
        pump_off()
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn off pump on exit
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure buzzer is off
    GPIO.cleanup()  # Clean up GPIO resources
