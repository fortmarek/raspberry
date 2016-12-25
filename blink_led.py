import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'



def blink(pin, speed):
    GPIO.output(pin, True)
    time.sleep(speed)
    GPIO.output(pin, False)
    time.sleep(speed)

    
def show(iterations):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)

    for i in range(0, iterations):
        blink(7, 0.1)
        time.sleep(0.1)
        blink(11, 0.1)
        time.sleep(0.1)

    GPIO.cleanup()

def test_blink():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    ## Ask user for total number of blinks and length of each blink
    iterations = input("Enter total number of times to blink: ")
    speed = input("Enter length of each blink(seconds): ")

    for i in range(0, iterations):
        blink(7, speed)

    GPIO.cleanup()

