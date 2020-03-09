from ClientGui.Logging.logger import Logger
from ClientGui.variables.Configuration import Configuration
import os
import shutil


class SendReceive:

    def __init__(self, socket, message):
        self.socket = socket
        self.message = message

    def send(self):
        self.socket.send(self.message.encode())

    def receive(self):
        mess = self.socket.recv(1024).decode()
        return mess

    def sendfile(self):
        Logger.info("Sending debug file to server")
        debug_file = "Logging/Logs"
        file_name = "/debug_" + Configuration.Username + ".log"
        with open(debug_file + file_name, 'rb') as f:
            sendData = f.read()
            print(sendData)
            self.socket.send(sendData)
        try:
            Logger().shutdownLogger()
            os.remove(debug_file + file_name)
        except OSError as e:
            Logger.error("Error: %s - %s." % (e.filename, e.strerror))
