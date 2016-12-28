import RPi.GPIO as GPIO
import flash


pins = []
def setup(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

