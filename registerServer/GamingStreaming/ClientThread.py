import socket
from threading import Thread
import picamera
from GamingStreaming.ControllerControl import ControllerControl
from GamingStreaming.GpioControl import GpioControl
from GamingStreaming.Streamer import Streamer
from Configuration import Configuration
from Database import Database
from time import sleep
import os

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
        global streamThread
        while self.Handler_running:
            try:
                data = self.connection.recv(2048).decode()
                if str(data).__contains__("_") is True:
                    ControllerControl(data)
                elif str(data).__contains__("StartStreamingServer"):
                    print(data)
                    video = str(data).split(',')
                    quality = video[1]
                    frames = video[2]
                    if Configuration.streaming_has_started is False:
                        GpioControl().turnOnXbox()
                        Configuration.streaming_has_started = True
                        streamThread = Streamer(quality, frames)
                        streamThread.start()
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
                elif str(data).__contains__("Stop"):
                    print("Stopping stream")
                    if Configuration.streaming_has_started is True:
                        Configuration.streaming_has_started = False
                        print("stopping")
                        streamThread.kill()
                        streamThread.join()
                    else:
                        print("stream has not started")
                elif str(data).__contains__("Connection Terminate"):
                    print(data)
                    if Configuration.streaming_has_started is True:
                        Configuration.streaming_has_started = False
                        print("stopping stream")
                        streamThread.kill()
                        streamThread.join()
                    break
                elif str(data).__contains__("*****************Start of Log********************") is True:
                    break
            except socket.error as serr:
                print(serr)
            except picamera.PiCameraError as p:
                print(p)
            except Exception as e:
                self.kill_handler()

        if self.ip is None:
            user_loggedin = "UPDATE userdetails set login = 'False' WHERE username='" + self.username + "';"
            Database.addIptoUser(user_loggedin)
            self.connection.send("Logged out".encode())
            logfile = Configuration.logDir + "debug_" + self.User + ".log"
            if os.path.exists(logfile):
                with open(logfile, 'ab') as f:
                    file = self.connection.recv(4024)
                    if not file:
                        print("No debug file received")
                    else:
                        print("Writing to file")
                        f.write(file)
            else:
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
            if os.path.exists(logfile):
                with open(logfile, 'ab') as f:
                    file = self.connection.recv(4024)
                    if not file:
                        print("No debug file received")
                    else:
                        print("Writing to file")
                        f.write(file)
            else:
                with open(logfile, 'wb') as f:
                    file = self.connection.recv(4024)
                    if not file:
                        print("No debug file received")
                    else:
                        print("Writing to file")
                        f.write(file)

    def kill_handler(self):
        Configuration.streaming_has_started = False
        print("Client Handler for " + str(self.User) + " Unexpectedly stopped")
        self.Handler_running = False

