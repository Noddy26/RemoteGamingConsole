from ClientGui.Configuration import Configuration
from ClientGui.Logging.logger import Logger
from ClientGui.Login import Login
from ClientGui.MainGui import MainGui
import socket

from ClientGui.Sendmessages import SendReceive


def main():
    Logger()
    sock = socket.socket()
    sock.connect((Configuration.ipAddress, Configuration.portNumber))

    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    message = host_ip
    SendReceive(sock, message).send()
    mess = SendReceive(sock, None).receive()
    if mess == "IP Found in database":
        Logger.info("IP Found in database")
        MainGui(None, sock).run()
    elif mess == "No Ip Found in database":
        Logger.info("No Ip Found in database")
        Login(sock).run()

if __name__ == '__main__':
    main()

