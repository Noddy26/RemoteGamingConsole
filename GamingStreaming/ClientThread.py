import base64
from threading import Thread
from registerServer.Database import Database


class ClientThread(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.connection = conn
        self.username = None
        self.ip = None
        print("New Thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = self.connection.recv(2048).decode()
            if str(data).__contains__("StartStreamingServer"):
                # TODO: Start Stream

                self.connection.send("StreamStarted".encode())
            elif str(data).__contains__("_"):
                parts = str(data).split("_")
                self.username = parts[0]
                raw_password = parts[1]
                if self.username is not None and parts[1] is not None:
                    if Database(self.username, raw_password, None).checkForUserPassword() is True:
                        print("Client Registered in database")
                        add_ip = "UPDATE userdetails set ipAddress = '" \
                                 + self.ip + "' WHERE username='" + self.username + "';"
                        user_loggedin = "UPDATE userdetails set Active = 'True' WHERE username='" + self.username + "';"
                        Database.addIptoUser(add_ip)
                        Database.addIptoUser(user_loggedin)
                        self.connection.send("Access Granted".encode())
                    else:
                        print("Client is not Registered in Database")
                        self.connection.send("Access Denied".encode())
                else:
                    print("Client entered no details")
                    self.connection.send("Access Denied".encode())
            elif str(data).__contains__("."):
                self.ip = data
                sql = "SELECT ipAddress FROM userdetails Where ipAddress='" + data + "';"
                user_loggedin = "UPDATE userdetails set Active = 'True' WHERE ipAddress='" + data + "';"
                if Database.checkIp(sql) is True:
                    print("IP Found in database")
                    self.connection.send("IP Found in database".encode())
                    Database.addIptoUser(user_loggedin)
            elif str(data).__contains__("StreamStop"):
                print("hello")
                #TODO: stop stream
                
            elif str(data).__contains__("Connection Terminated"):
                if self.ip is None:
                    user_loggedin = "UPDATE userdetails set Active = 'False' WHERE username='" + self.username + "';"
                    Database.addIptoUser(user_loggedin)
                else:
                    user_loggedin = "UPDATE userdetails set Active = 'False' WHERE ipAddress='" + self.ip + "';"
                    Database.addIptoUser(user_loggedin)

            else:
                print("Connection finished")
                break
