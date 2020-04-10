import smbus
import time


class ControllerOneControl:

    def __init__(self, data):
        self.check(data)
        self.address = 0x04
        self.bus = smbus.SMBus(1)

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
        self.writeData("U1")
        time.sleep(0.01)
        self.writeData("*")

    def DpadDown(self):
        self.writeData("D1")
        time.sleep(0.01)
        self.writeData("*")

    def DpadLeft(self):
        self.writeData("F1")
        time.sleep(0.01)
        self.writeData("*")

    def DpadRight(self):
        self.writeData("G1")
        time.sleep(0.01)
        self.writeData("*")

    def L3Button(self):
        self.writeData("<1")
        time.sleep(0.01)
        self.writeData("*")

    def L2Button(self):
        self.writeData("{1")
        time.sleep(0.01)
        self.writeData("*")

    def L1Button(self):
        self.writeData("[1")
        time.sleep(0.01)
        self.writeData("*")

    def selectButton(self):
        self.writeData("Z1")
        time.sleep(0.01)
        self.writeData("*")

    def homeButton(self):
        self.writeData("P1")
        time.sleep(0.01)
        self.writeData("*")

    def startButton(self):
        self.writeData("Y1")
        time.sleep(0.01)
        self.writeData("*")

    def R1Button(self):
        self.writeData("]1")
        time.sleep(0.01)
        self.writeData("*")

    def R2Button(self):
        self.writeData("}1")
        time.sleep(0.01)
        self.writeData("*")

    def R3Button(self):
        self.writeData(">1")
        time.sleep(0.01)
        self.writeData("*")

    def XButton(self):
        self.writeData("S1")
        time.sleep(0.01)
        self.writeData("*")

    def YButton(self):
        self.writeData("T1")
        time.sleep(0.01)
        self.writeData("*")

    def BButton(self):
        self.writeData("O1")
        time.sleep(0.01)
        self.writeData("*")

    def AButton(self):
        self.writeData("X1")
        time.sleep(0.01)
        self.writeData("*")

    def leftStickX(self, val):
        self.writeData("L" + val)

    def leftStickY(self, val):
        self.writeData("l" + val)

    def rightStickX(self, val):
        self.writeData("R" + val)

    def rightStickY(self, val):
        self.writeData("r" + val)

    def writeData(self, value):
        byteValue = self.StringToBytes(value)
        self.bus.write_i2c_block_data(self.address, 0x00, byteValue)
        return -1

    def StringToBytes(self, val):
            retVal = []
            for c in val:
                    retVal.append(ord(c))
            return retVal
