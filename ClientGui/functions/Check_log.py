import os
from ClientGui.Logging.logger import Logger
from ClientGui.functions.Sendmessages import SendReceive


class CheckLog:

    def __init__(self, sock, ip):
        if os.path.exists(r"Logging\Logs\debug_User.log"):
            print("ya")
            SendReceive(sock, None).sendfile()
            user = SendReceive(sock, None).receive()
            if user == "send ip":
                print("sending")
                SendReceive(sock, ip).send()
