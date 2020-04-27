import os
from ClientGui.Logging.logger import Logger
from ClientGui.functions.Sendmessages import SendReceive


class CheckLog:

    def __init__(self, sock):
        if os.path.exists(r"Logging\Logs\debug_User.log"):
            SendReceive(sock, None).sendfile()
