import RPi.GPIO as GPIO


def flash(pin):
    GPIO.output(pin, True)

def stop(pin):
    GPIO.output(pin, False)

def flash_multiple(pins):
    for pin in pins:
        GPIO.output(pin, True)

def stop_multiple(pins):
    for pin in pins:
        GPIO.output(pin, False)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)

    pin = int(input("Which pin:"))
    GPIO.setup(pin, GPIO.OUT)

    flash(pin)

    wait_for_stop = input("Enter to stop")
    stop(pin)

    GPIO.cleanup()
