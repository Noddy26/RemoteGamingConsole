from ClientGui.Login import Login
from ClientGui.MainGui import MainGui
import socket

from registerServer.Configuration import Configuration


def main():
    sock = socket.socket()
    port = 2003
    sock.connect((Configuration.ipAddress, port))

    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    message = host_ip
    sock.send(message.encode())
    mess = sock.recv(1024).decode()
    if mess == "IP Found in database":
        MainGui(None, sock).run()
    elif mess == "No Ip Found in database":
        Login(sock).run()

if __name__ == '__main__':
    main()

