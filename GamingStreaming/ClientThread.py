from tkinter import messagebox

import pyfirmata
from threading import Thread

from GamingStreaming.ControllerControl import ControllerControl
from GamingStreaming.GpioControl import GpioControl
from GamingStreaming.Streamer import Streamer
from Configuration import Configuration
from Database import Database
from time import sleep


class ClientThread(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.connection = conn
        self.username = None
        self.ip = None
        self.User = None
        self.Handler_running = True
        print("New Thread started for " + ip + ":" + str(port))

    def run(self):

        while self.Handler_running:
            try:
                data = self.connection.recv(2048).decode()
                if str(data).__contains__("StartStreamingServer"):
                    print(data)
                    video = str(data).split(',')
                    quality = video[1]
                    frames = video[2]
                    if Configuration.streaming_has_started is False or Configuration.server_running is False:
                        GpioControl().turnOnXbox()
                        self.streamThread = Streamer(quality, frames)
                        self.streamThread.setDaemon(True)
                        self.streamThread.start()
                        sleep(5)
                        print("stream started")
                        self.connection.send("StreamStarted".encode())
                    else:
                        print("Stream already started")
                        self.connection.send("StreamalreadyStarted".encode())
                elif str(data).__contains__("+"):
                    parts = str(data).split("+")
                    self.username = parts[0]
                    raw_password = parts[1]
                    if self.username is not None and parts[1] is not None:
                        if Database(self.username, raw_password, None).checkForUserPassword() is True:
                            print("Client Registered in database")
                            add_ip = "UPDATE userdetails set ipAddress = '" \
                                     + self.ip + "' WHERE username='" + self.username + "';"
                            user_loggedin = "UPDATE userdetails set login = 'True' WHERE username='" + self.username + "';"
                            Database.addIptoUser(add_ip)
                            Database.addIptoUser(user_loggedin)
                            self.User = self.username
                            self.connection.send("Access Granted".encode())
                        else:
                            print("Client is not Registered in Database")
                            self.connection.send("Access Denied".encode())
                    else:
                        print("Client entered no details")
                        self.connection.send("Access Denied".encode())
                elif str(data).__contains__("."):
                    self.ip = data
                    sql = "SELECT username FROM userdetails Where ipAddress='" + data + "';"
                    user_loggedin = "UPDATE userdetails set login = 'True' WHERE ipAddress='" + data + "';"
                    user = Database.checkIp(sql)
                    if user is not None:
                        self.User = user
                        print("IP Found in database")
                        self.connection.send("IP Found in database".encode())
                        Database.addIptoUser(user_loggedin)
                        print("User Logged in")
                    else:
                        self.connection.send("No Ip Found in database".encode())
                elif str(data).__contains__("StreamStop"):
                    print("Stopping stream")
                    if Configuration.streaming_has_started is True:
                        Streamer(None, None).stop()
                        self.streamThread.join()
                elif str(data).__contains__("Connection Terminate"):
                    print(data)
                    if Configuration.streaming_has_started is True:
                        Streamer(None, None).stop()
                        self.streamThread.join()
                    break
                elif str(data).__contains__("_") is True:
                    ControllerControl(data)
                elif str(data).__contains__("b'") is True:
                    break
            except:
                self.stop()

        if self.ip is None:
            user_loggedin = "UPDATE userdetails set login = 'False' WHERE username='" + self.username + "';"
            Database.addIptoUser(user_loggedin)
            self.connection.send("Logged out".encode())
            logfile = Configuration.logDir + "debug_" + self.User + ".log"
            with open(logfile, 'wb') as f:
                file = self.connection.recv(4024)
                if not file:
                    print("No debug file received")
                else:
                    print("Writing to file")
                    f.write(file)
        else:
            user_loggedin = "UPDATE userdetails set login = 'False' WHERE ipAddress='" + self.ip + "';"
            Database.addIptoUser(user_loggedin)
            self.connection.send("Logged out".encode())
            logfile = Configuration.logDir + "debug_" + self.User + ".log"
            with open(logfile, 'wb') as f:
                file = self.connection.recv(4024)
                if not file:
                    print("No debug file received")
                else:
                    print("Writing to file")
                    f.write(file)

    def stop(self):
        print("Client Handler for " + str(self.User) + " Unexpectedly stopped")
        self.Handler_running = False

