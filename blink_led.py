import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def Blink(numTimes,speed):
    for i in range(0,numTimes):
        GPIO.output(7,True)
        print("ON")
        time.sleep(speed)
        print("OFF")
        GPIO.output(7,False)
        time.sleep(speed)
    print("DONE")
    GPIO.cleanup()

if __name__ == "__main__":

    ## Ask user for total number of blinks and length of each blink
    iterations = input("Enter total number of times to blink: ")
    speed = input("Enter length of each blink(seconds): ")

    ## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
    Blink(int(iterations),float(speed))