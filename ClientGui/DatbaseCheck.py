import socket

class DatabaseCheck:

    def __init__(self, user, password, message, socks):
        self.sock = socks
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
            return False

    def start_Stream(self):
        self.sock.send(self.message.encode())
        mess = self.sock.recv(1024).decode()
        if mess == "StreamStarted":
            print(mess)
            return True

    def disconnect(self):
        self.sock.send(self.message.encode())
        print(self.message)
        mess = self.sock.recv(1024).decode()
        print(mess)
        if mess == "Logged out":
            return True
        else:
            return False
