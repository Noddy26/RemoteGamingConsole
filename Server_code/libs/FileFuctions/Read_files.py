from libs.Console.Terminal import Output


class ReadFiles():

    def __init__(self, file, data):
        self.data = data
        self.file = file


    def appendbinary(self):
        with open(self.file, 'a') as f:
            f.write("\n")
        f.close()
        with open(self.file, 'ab') as f:
            file = self.data
            if not file:
                Output.red("No debug file received")
            else:
                Output.yellow("Writing to file")
                f.write(file)
        f.close()

    def writebinary(self):
        with open(self.file, 'wb') as f:
            if not self.data:
                Output.red("No debug file received")
            else:
                Output.yellow("Writing to file")
                f.write(self.data)
        f.close()
