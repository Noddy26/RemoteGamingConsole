import RPi.GPIO as GPIO
import time

from Configuration import Configuration


class GpioControl():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        print("Gpio Control")

    def gpiohigh(self):
        if Configuration.pins_high is False:
            Configuration.pins_high = True
            pins = [2, 3, 4, 7, 8, 9, 12, 17, 21, 22, 23, 24, 25, 26, 27]
            for each in pins:
                GPIO.setup(each, GPIO.OUT)
                GPIO.output(each, 1)

    def gpiolow(self):
        Configuration.pins_high = False
        pins = [2, 3, 4, 7, 8, 9, 12, 17, 21, 22, 23, 24, 25, 26, 27]
        for each in pins:
            GPIO.setup(each, GPIO.OUT)
            GPIO.output(each, 0)

    def turnOnXbox(self):
        GPIO.setup(2, GPIO.OUT)
        GPIO.output(2, 0)
        time.sleep(0.5)
        GPIO.output(2, 1)