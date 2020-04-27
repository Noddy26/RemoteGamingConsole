import picamera
import socket
import os
from threading import Thread
from multiprocessing import Process
from libs.Console.Terminal import Output
from libs.Database_functions.Database import Database
from libs.FileFuctions.Read_files import ReadFiles
from libs.GamingStreaming.App_keys import AppKeys
from libs.GamingStreaming.ControllerOneControl import ControllerOneControl
from libs.GamingStreaming.Streamer import Streamer
from libs.GamingStreaming.TurnOnConsole import TurnOnConsole
from libs.variables.Configuration import Configuration
from libs.Server_logging.Logging import Logger


class ClientThread(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.connection = conn
        self.username = None
        self.User = None
        self.Handler_running = True
        Configuration.secondplayer = False
        print("New Thread started for " + ip + ":" + str(port))

    def run(self):
        while self.Handler_running:
            try:
                data = self.connection.recv(2048).decode()
                self.keys(data)
            except socket.error as serr:
                Output.red(serr)
            except picamera.PiCameraError as p:
                Output.red(p)
            except Exception as e:
                Output.red(e)
                self.kill_handler()

    def keys(self, incoming):

        Dictionary = {AppKeys.controller_key: self.controller, AppKeys.Login_key: self.checkDetails,
                      AppKeys.StartStrem_key: self.startstream, AppKeys.ip_key: self.checkip,
                      AppKeys.StopStrem_key: self.stopstream, AppKeys.Terminate_key: self.terminate,
                      AppKeys.Version_key: self.version, AppKeys.LogFile_key: self.getDebugfile,
                      AppKeys.enable_two_player: self.enable_two_player,
                      AppKeys.disable_two_player: self.disable_two_player}

        for key in Dictionary:
            if incoming.__contains__(key):
                function = Dictionary[key]
                function(incoming)
                break

    def controller(self, data):
        ControllerOneControl(data)

    def checkDetails(self, data):
        parts = str(data).split("+")
        self.username = parts[0]
        raw_password = parts[1]
        clienttype = parts[2]
        if clienttype == "Gui":
            Configuration.ClientTypeGui = True
        if self.username is not None and parts[1] is not None:
            if Database(self.username, raw_password, None).checkForUserPassword() is True:
                Output.green("Client Registered in database")
                add_ip = AppKeys.AddIp % (self.ip, self.username)
                user_loggedin = AppKeys.Loggedin % self.username
                Database.addIptoUser(add_ip)
                Database.addIptoUser(user_loggedin)
                self.User = self.username
                if Configuration.ClientTypeGui == True:
                    self.connection.send(AppKeys.Gui_Access.encode())
                else:
                    self.connection.send(AppKeys.Access.encode())
            else:
                self.User = self.username
                Output.yellow("Client is not Registered in Database")
                if Configuration.ClientTypeGui == True:
                    self.connection.send(AppKeys.Gui_denied.encode())
                else:
                    self.connection.send(AppKeys.denied.encode())
        else:
            Output.yellow("Client is not Registered in Database")
            if Configuration.ClientTypeGui == True:
                self.connection.send(AppKeys.Gui_denied.encode())
            else:
                self.connection.send(AppKeys.denied.encode())

    def startstream(self, data):
        video = str(data).split(',')
        quality = video[1]
        frames = video[2]
        if Configuration.streaming_has_started is False:
            TurnOnConsole().turnOnXbox()
            Configuration.streaming_has_started = True
            self.process = Process(target=Streamer(), args=(quality, frames)).start()
            Output.yellow("stream started")
            if Configuration.ClientTypeGui == True:
                self.connection.send(AppKeys.Gui_streamStared.encode())
            else:
                self.connection.send(AppKeys.streamStared.encode())

    def stopstream(self, data):
        print("Stopping stream")
        if Configuration.streaming_has_started is True:
            Configuration.streaming_has_started = False
            Output.yellow("stopping")
            self.process.kill()
            self.process.join()
        else:
            print("stream has not started")

    def checkip(self, data):
        get = data.split("`")
        self.ip = get[0]
        if get[1] == "Gui":
            Configuration.ClientTypeGui = True
        sql = AppKeys.GetUser % data
        user_loggedin = AppKeys.Loggedin % data
        user = Database.checkIp(sql)
        if user is not None:
            self.User = user
            Output.yellow("IP Found in database")
            if Configuration.ClientTypeGui == True:
                self.connection.send(AppKeys.Gui_Ip_Found.encode())
            else:
                self.connection.send(AppKeys.Ip_Found.encode())
            Database.addIptoUser(user_loggedin)
            Output.yellow("User Logged in")
        else:
            if Configuration.ClientTypeGui == True:
                self.connection.send(AppKeys.Gui_Ip_Not_Found.encode())
            else:
                self.connection.send(AppKeys.Ip_Not_Found.encode())

    def enable_two_player(self, data):
        Configuration.secondplayer = True

    def disable_two_player(self, data):
        Configuration.secondplayer = False

    def version(self, data):
        if Configuration.ClientTypeGui == True:
            self.connection.send(str(Configuration.versionGui).encode())
        else:
            self.connection.send(str(Configuration.versionApp).encode())

    def terminate(self, data):
        if Configuration.streaming_has_started is True:
            Configuration.streaming_has_started = False
            Logger.info("stopping stream")
            self.process.kill()
            self.process.join()
        self.getDebugfile(AppKeys.LogFile_key)

    def getDebugfile(self, data):
        if self.ip is None:
            user_loggedin = AppKeys.Loggedout % self.username.replace("'", "")
            Database.addIptoUser(user_loggedin)
            if Configuration.ClientTypeGui == True:
                self.connection.send(AppKeys.Gui_Logout.encode())
            else:
                self.connection.send(AppKeys.Logout.encode())
            logfile = Configuration.logDir + "debug_" + self.User + ".log"
            if os.path.exists(logfile):
                files = self.connection.recv(4024)
                ReadFiles(logfile, files).appendbinary()
            else:
                files = self.connection.recv(4024)
                ReadFiles(logfile, files).writebinary()
        else:
            user_loggedin = AppKeys.Loggedout % self.ip
            Database.addIptoUser(user_loggedin)
            if Configuration.ClientTypeGui == True:
                self.connection.send(AppKeys.Gui_Logout.encode())
            else:
                self.connection.send(AppKeys.Logout.encode())
            logfile = Configuration.logDir + "debug_" + self.User.replace("'", "") + ".log"
            if os.path.exists(logfile):
                files = self.connection.recv(4024)
                ReadFiles(logfile, files).appendbinary()
            else:
                files = self.connection.recv(4024)
                ReadFiles(logfile, files).writebinary()

    def kill_handler(self):
        Configuration.streaming_has_started = False
        print("Client Handler for " + str(self.User) + " Unexpectedly stopped")
        self.Handler_running = False
        if Configuration.ClientTypeGui == True:
            self.connection.send(AppKeys.Gui_Logout.encode())
        else:
            self.connection.send(AppKeys.Logout.encode())
