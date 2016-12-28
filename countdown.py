import RPi.GPIO as GPIO
import flash
import time


#Pin equivalents to digit marks
a = 7
b = 11
c = 12
d = 13
e = 15
f = 16
g = 18
dp = 19

parts = [a, b, c, d, e, f, g, dp]

digit_dict = {
    0: [[a, b, c, d, e, f], [g, dp]],
    1: [[b, c], [a, d, e, f, g, dp]],
    2: [[a, b, d, e, g], [c, f, dp]],
    3: [[a, b, c, d, g], [e, f, dp]],
    4: [[b, c, f, g], [a, d, e, dp]],
    5: [[a, c, d, f, g], [b, e, dp]],
    6: [[a, c, d, e, f, g], [b, dp]],
    7: [[a, b, c], [d, e, f, g, dp]],
    8: [[a, b, c, d, e, f, g], [dp]],
    9: [[a, b, c, d, f, g], [e, dp]]
}

def setup(pin):
    GPIO.setmode(GPIO.BOARD)
    for part in parts:
        GPIO.setup(part, GPIO.OUT)
        GPIO.output(part, True)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

def clean(pin):
    flash.stop_multiple(parts)
    flash.stop(pin)
    GPIO.cleanup()

def tick_number(n):
    dict = digit_dict[n]
    flash.stop_multiple(dict[0])
    flash.flash_multiple(dict[1])

def countdown():
    for i in range(0, 10):
        tick_number(i)
        time.sleep(1)