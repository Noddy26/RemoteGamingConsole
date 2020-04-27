import errno
from tkinter import Tk, messagebox
import time
from ClientGui.functions.Check_log import CheckLog
from ClientGui.functions.GetLocation import UserLocation
from ClientGui.variables.Configuration import Configuration
from ClientGui.Logging.logger import Logger
from ClientGui.Display.Login import Login
from ClientGui.Display.MainGui import MainGui
import socket
from ClientGui.functions.Sendmessages import SendReceive


def main():

    sock = socket.socket()
    sock.connect((Configuration.ipAddress, Configuration.portNumber))
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    #CheckLog(sock, host_ip)
    Logger()
    UserLocation().run()
    message = host_ip + "`Gui"
    print(message)
    SendReceive(sock, message).send()
    mess = SendReceive(sock, None).receive()
    print(mess)
    if mess == "IP Found in database":
        Logger.info("IP Found in database")
        MainGui(None, sock).run()
    elif mess == "No Ip Found in database":
        Logger.info("No Ip Found in database")
        Login(sock).run()

if __name__ == '__main__':
    try:
        main()
    except socket.error as serr:
        if Configuration.Logstarted == True:
            Logger.error(serr)
        if serr.errno == errno.ECONNREFUSED:
            Tk().withdraw()
            messagebox.showerror("ERROR", "Can not connect to server")
        else:
            Tk().withdraw()
            messagebox.showerror("ERROR", "Something went wrong with the server")
    except Exception as e:
        if Configuration.Logstarted == True:
            Logger.error(e)
        Tk().withdraw()
        messagebox.showerror("ERROR", "Something went wrong with the server")
