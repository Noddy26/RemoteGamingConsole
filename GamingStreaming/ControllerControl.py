import RPi.GPIO as GPIO


class ControllerControl():

    def __init__(self, data):
        pins = [2, 3, 4, 7, 8, 9, 12, 17, 21, 22, 23, 24, 25, 26, 27]
        GPIO.setmode(GPIO.BCM)
        for each in pins:
            GPIO.setup(each, GPIO.OUT)
            GPIO.output(each, 1)
        print("Controller Class")
        self.check(data)

    def check(self, data):

        new = data.split("_")
        buttonpressed = new[2]

        buttons = {"1": self.DpadUp, "2": self.DpadDown, "3": self.DpadLeft, "4": self.DpadRight, "5": self.L3Button,
                   "6": self.L1Button, "7": self.selectButton, "8": self.homeButton, "9": self.startButton,
                   "10": self.R1Button, "11": self.R3Button, "12": self.XButton, "13": self.YButton,
                   "14": self.BButton, "15": self.AButton}

        if buttonpressed in buttons:
            function = buttons[buttonpressed]
            function()

    def DpadUp(self):
        print("Dpad up")
        GPIO.output(26, 0)

    def DpadDown(self):
        GPIO.output(21, 0)

    def DpadLeft(self):
        GPIO.output(12, 0)

    def DpadRight(self):
        GPIO.output(7, 0)

    def L3Button(self):
        GPIO.output(8, 0)

    def L1Button(self):
        GPIO.output(25, 0)

    def selectButton(self):
        GPIO.output(24, 0)

    def homeButton(self):
        GPIO.output(23, 0)

    def startButton(self):
        GPIO.output(2, 0)

    def R1Button(self):
        GPIO.output(3, 0)

    def R3Button(self):
        GPIO.output(4, 0)

    def XButton(self):
        GPIO.output(17, 0)

    def YButton(self):
        GPIO.output(27, 0)

    def BButton(self):
        GPIO.output(22, 0)

    def AButton(self):
        GPIO.output(9, 0)
