import time

from Logging.logger import Logger
from variables.Configuration import Configuration
import os
import shutil


class SendReceive:

    def __init__(self, socket, message):
        self.socket = socket
        self.message = message

    def send(self):
        if self.message.__contains__("+"):
            Logger.info("sending: " + "***************")
        else:
            Logger.info("sending: " + self.message)
        self.socket.send(self.message.encode())

    def receive(self):
        mess = self.socket.recv(1024).decode()
        Logger.info("received: " + mess)
        return mess

    def sendfile(self):
        debug_file = Configuration.log_path
        file_name = "/debug_User.log"
        if Configuration.Logstarted == True:
            Configuration.end_time = time.time()
            Total_time = Configuration.start_time - Configuration.end_time
            total = str(Total_time).replace("-", "")
            Logger.info("Sending debug file to server")
        with open(Configuration.log_path + file_name, "a") as f:
            if Configuration.Logstarted == True:
                f.write("Total Time online: %s" % total)
            f.write("\n*****************End of Log**********************")
        f.close()
        with open(debug_file + file_name, 'rb') as f:
            sendData = f.read()
            self.socket.send(sendData)
        try:
            if Configuration.Logstarted == True:
                Logger().shutdownLogger()
            os.remove(debug_file + file_name)
        except OSError as e:
            Logger.error("Error: %s - %s." % (e.filename, e.strerror))
