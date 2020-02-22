
class SendReceive:

    def __init__(self, socket, message):
        self.socket = socket
        self.message = message

    def send(self):
        self.socket.send(self.message.encode())

    def receive(self):
        mess = self.socket.recv(1024).decode()
        return mess
