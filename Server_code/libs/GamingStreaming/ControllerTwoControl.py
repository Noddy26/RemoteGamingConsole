import smbus
import time
from libs.Console.Terminal import Output


class ControllerOneControl:

    def __init__(self, data):
        self.address = 0x05
        self.bus = smbus.SMBus(1)
        self.data = data
        self.value = None
        self.check(data)

    def check(self, data):
        new = data.split("_")
        buttonpressed = new[2]
        if len(new) > 3:
            self.value = new[3]

        buttons = {"1": self.DpadUp, "2": self.DpadDown, "3": self.DpadLeft, "4": self.DpadRight, "5": self.L3Button,
                   "6": self.L1Button, "7": self.selectButton, "8": self.homeButton, "9": self.startButton,
                   "10": self.R1Button, "11": self.R3Button, "12": self.XButton, "13": self.YButton,
                   "14": self.BButton, "15": self.AButton, "16": self.L2Button, "17": self.R2Button,
                   "18": self.leftStickX, "19": self.leftStickY, "20": self.rightStickX, "21": self.rightStickY}

        if buttonpressed in buttons:
            function = buttons[buttonpressed]
            try:
                function()
            except IOError as e:
                Output.red(e)

    def DpadUp(self):
        self.writeData("U1")
        time.sleep(0.020)
        self.writeData("*")

    def DpadDown(self):
        self.writeData("D1")
        time.sleep(0.020)
        self.writeData("*")

    def DpadLeft(self):
        self.writeData("F1")
        time.sleep(0.020)
        self.writeData("*")

    def DpadRight(self):
        self.writeData("G1")
        time.sleep(0.020)
        self.writeData("*")

    def L3Button(self):
        self.writeData("<1")
        time.sleep(0.020)
        self.writeData("*")

    def L2Button(self):
        if int(self.value) == 1:
            self.writeData("{1")
        elif int(self.value) == 0:
            self.reset()

    def L1Button(self):
        self.reset()
        self.writeData("[1")

    def selectButton(self):
        self.writeData("Z1")
        time.sleep(0.020)
        self.writeData("*")

    def homeButton(self):
        self.writeData("P1")
        time.sleep(0.020)
        self.writeData("*")

    def startButton(self):
        self.writeData("Y1")
        time.sleep(0.020)
        self.writeData("*")

    def R1Button(self):
        self.writeData("]1")
        time.sleep(0.020)
        self.writeData("]0")

    def R2Button(self):
        if int(self.value) == 1:
            self.writeData("}1")
        elif int(self.value) == 0:
            self.reset()

    def R3Button(self):
        self.writeData(">1")
        time.sleep(0.020)
        self.writeData("*")

    def XButton(self):
        self.writeData("S1")
        time.sleep(0.020)
        self.writeData("S0")

    def YButton(self):
        self.writeData("T1")
        time.sleep(0.020)
        self.writeData("*")

    def BButton(self):
        self.writeData("O1")
        time.sleep(0.020)
        self.writeData("*")

    def AButton(self):
        self.writeData("X1")
        time.sleep(0.020)
        self.writeData("*")

    def leftStickX(self):
        new = self.data.split("_")
        new_val1 = self.remapping(int(new[3]))
        self.writeData("L" + str(int(new_val1)))

    def leftStickY(self):
        new = self.data.split("_")
        new_val2 = self.remapping(int(new[3]))
        self.writeData("l" + str(int(new_val2)))

    def rightStickX(self):
        new = self.data.split("_")
        new_val3 = self.remapping(int(new[3]))
        self.writeData("R" + str(int(new_val3)))

    def rightStickY(self):
        new = self.data.split("_")
        new_val4 = self.remapping(int(new[3]))
        self.writeData("r" + str(int(new_val4)))

    def writeData(self, value):
        byteValue = self.StringToBytes(value)
        self.bus.write_i2c_block_data(self.address, 0x00, byteValue)
        return -1

    def StringToBytes(self, val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal

    def reset(self):
        self.writeData("*")
        print("reset done")

    def remapping(self, OldValue):
        OldMax = 32767
        OldMin = -32767
        NewMax = 254
        NewMin = 0

        OldRange = (OldMax - OldMin)
        NewRange = (NewMax - NewMin)
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        return int(NewValue)

