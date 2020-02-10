import socket

from ClientGui.Configuration import Configuration


class DatabaseCheck:

    def __init__(self, user, password, message):
        self.sock = socket.socket()
        self.port = Configuration.portNumber
        self.sock.connect((Configuration.ipAddress, self.port))
        self.user = user
        self.password = password
        self.message = message

    def check_user(self):
        message = self.user + "_" + self.password
        self.sock.send(message.encode())
        mess = self.sock.recv(1024).decode()
        if mess == "Access Granted":
            self.sock.close()
            return True
        else:
            self.sock.close()
            return False

    def start_Stream(self):
        self.sock.send(self.message.encode())
        mess = self.sock.recv(1024).decode()
        if mess == "StreamStarted":
            print(mess)
            return True

    def check_ip(self):
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        message = host_ip
        self.sock.send(message.encode())
        mess = self.sock.recv(1024).decode()
        if mess == "IP Found in database":
            return True
        else:
            return False
