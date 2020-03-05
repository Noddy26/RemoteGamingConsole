import base64
from threading import Thread

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
        print("New Thread started for " + ip + ":" + str(port))

    def run(self):

        while True:
            data = self.connection.recv(2048).decode()
            print(data)
            if str(data).__contains__("StartStreamingServer"):
                print(data)
                video = str(data).split(',')
                quality = video[1]
                frames = video[2]
                if Configuration.streaming_has_started is False or Configuration.server_running is False:
                    self.streamThread = Streamer(quality, frames)
                    self.streamThread.start()
                    self.streamThread.setDaemon(True)
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
                print(data)
                print("Buttons")
            elif str(data).__contains__("poo") is True:
                print("poo")
                # this is for get the debug file

        if self.ip is None:
            user_loggedin = "UPDATE userdetails set login = 'False' WHERE username='" + self.username + "';"
            Database.addIptoUser(user_loggedin)
            self.connection.send("Logged out".encode())
            logfile = "User_logs/debug_" + self.User + ".log"
            with open(logfile, 'wb') as f:
                file = self.connection.recv(1024)
                if not file:
                    print("No debug file received")
                else:
                    f.write(file)
        else:
            user_loggedin = "UPDATE userdetails set login = 'False' WHERE ipAddress='" + self.ip + "';"
            Database.addIptoUser(user_loggedin)
            self.connection.send("Logged out".encode())
            logfile = "User_logs/debug_" + self.User + ".log"
            with open(logfile, 'wb') as f:
                file = self.connection.recv(1024)
                if not file:
                    print("No debug file received")
                else:
                    f.write(file)
