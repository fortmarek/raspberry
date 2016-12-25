import blink_led as blink
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
blink.blink(7, 1)
time.sleep(1)
blink.blink(7, 1)

GPIO.cleanup()