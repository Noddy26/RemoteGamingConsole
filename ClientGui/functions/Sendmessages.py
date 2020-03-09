import time

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
        debug_file = "Logging/Logs"
        file_name = "/debug_" + Configuration.Username + ".log"
        Configuration.end_time = time.time()
        Total_time = Configuration.start_time - Configuration.end_time
        Logger.info("Sending debug file to server")
        with open("Logging/logs/" + file_name, "a") as f:
            f.write("Total Time online: %s" % Total_time)
            f.write("\n*****************End of Log********************")
        f.close()
        with open(debug_file + file_name, 'rb') as f:
            sendData = f.read()
            self.socket.send(sendData)
        try:
            Logger().shutdownLogger()
            os.remove(debug_file + file_name)
        except OSError as e:
            Logger.error("Error: %s - %s." % (e.filename, e.strerror))
