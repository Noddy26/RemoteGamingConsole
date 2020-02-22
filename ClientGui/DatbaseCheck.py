from ClientGui.Logging.logger import Logger
from ClientGui.Sendmessages import SendReceive


class DatabaseCheck:

    def __init__(self, user, password, message, socks):
        self.sock = socks
        self.user = user
        self.password = password
        self.message = message

    def check_user(self):
        message = self.user + "_" + self.password
        SendReceive(self.sock, message).send()
        mess = SendReceive(self.sock, None).receive()
        if mess == "Access Granted":
            Logger.error("Access Granted")
            return True
        else:
            Logger.error("incorrect details logged")
            return False

    def start_Stream(self):
        SendReceive(self.sock, self.message).send()
        mess = SendReceive(self.sock, None).receive()
        if mess == "StreamStarted":
            Logger.error("Stream has started")
            # TODO: START TIMER HERE FOR WHEN STREAM HAS STARTED
            return True
        return False

    def disconnect(self):
        SendReceive(self.sock, self.message).send()
        print(self.message)
        mess = SendReceive(self.sock, None).receive()
        print(mess)
        if mess == "Logged out":
            Logger.error("Logged out from server")
            print("return")
            return True
        else:
            Logger.error("Cannot log out from server")
            return False
