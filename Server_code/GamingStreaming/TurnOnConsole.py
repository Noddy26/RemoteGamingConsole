import smbus
import time


class TurnOnConsole:

    def __init__(self):
        self.address = 0x04
        self.bus = smbus.SMBus(1)

    def turnOnXbox(self):
        self.writeData("P1")
        time.sleep(0.01)
        self.writeData("*")

    def writeData(self, value):
        byteValue = self.StringToBytes(value)
        self.bus.write_i2c_block_data(self.address, 0x00, byteValue)
        return -1

    def StringToBytes(self, val):
        retVal = []
        for c in val:
            retVal.append(ord(c))
        return retVal