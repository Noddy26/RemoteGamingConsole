import RPi.GPIO as GPIO
import time


class GpioControl():

    def __init__(self):
        print("Gpio Control")

    def gpiohigh(self):
        pins = [2, 3, 4, 7, 8, 9, 12, 17, 21, 22, 23, 24, 25, 26, 27]
        GPIO.setmode(GPIO.BCM)
        for each in pins:
            GPIO.setup(each, GPIO.OUT)
            GPIO.output(each, 1)

    def gpiolow(self):
        pins = [2, 3, 4, 7, 8, 9, 12, 17, 21, 22, 23, 24, 25, 26, 27]
        GPIO.setmode(GPIO.BCM)
        for each in pins:
            GPIO.setup(each, GPIO.OUT)
            GPIO.output(each, 0)

    def turnOnXbox(self):
        GPIO.output(2, 0)
        time.sleep(0.5)
        GPIO.output(2, 1)