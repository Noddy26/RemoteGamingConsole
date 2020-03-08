import pyfirmata

class ControllerControl():

    def __init__(self, data):
        self.ardunio = pyfirmata.Arduino('/dev/ttyACM0')
        data.split = data.split("_")
        new_data = data.split[1]
        self.run(new_data)

    def run(self, data):
        switcher = {
            1: self.DpadUp(),
            2: self.DpadDown(),
            3: self.DpadLeft(),
            4: self.DpadRight(),
            5: self.L3Button(),
            6: self.L1Button(),
            7: self.selectButton(),
            8: self.homeButton(),
            9: self.startButton(),
            10: self.R1Button(),
            11: self.R3Button(),
            12: self.XButton(),
            13: self.YButton(),
            14: self.BButton(),
            15: self.AButton()
        }
        print(switcher.get(data, "Invalid Button Press"))

    def DpadUp(self):
        print("Dpad up")
        pinA0 = self.ardunio.get_pin('a:0:o')
        pinA0.write(0)

    def DpadDown(self):
        pin0 = self.ardunio.get_pin('d:0:o')
        pin0.write(0)

    def DpadLeft(self):
        pin1 = self.ardunio.get_pin('d:1:o')
        pin1.write(0)

    def DpadRight(self):
        pin2 = self.ardunio.get_pin('d:2:o')
        pin2.write(0)

    def L3Button(self):
        pin3 = self.ardunio.get_pin('d:3:o')
        pin3.write(0)

    def L1Button(self):
        pin4 = self.ardunio.get_pin('d:4:o')
        pin4.write(0)

    def selectButton(self):
        pin5 = self.ardunio.get_pin('d:5:o')
        pin5.write(0)

    def homeButton(self):
        pin6 =  self.ardunio.get_pin('d:6:o')
        pin6.write(0)

    def startButton(self):
        pin7 = self.ardunio.get_pin('d:7:o')
        pin7.write(0)

    def R1Button(self):
        pin8 = self.ardunio.get_pin('d:8:o')
        pin8.write(0)

    def R3Button(self):
        pin9 = self.ardunio.get_pin('d:9:o')
        pin9.write(0)

    def XButton(self):
        pin10 = self.ardunio.get_pin('d:10:o')
        pin10.write(0)

    def YButton(self):
        pin11 = self.ardunio.get_pin('d:11:o')
        pin11.write(0)

    def BButton(self):
        pin12 = self.ardunio.get_pin('d:12:o')
        pin12.write(0)

    def AButton(self):
        pin13 = self.ardunio.get_pin('d:13:o')
        pin13.write(0)
