import errno
from tkinter import messagebox, Tk
from functions.Check_log import CheckLog
from functions.GetLocation import UserLocation
from variables.Configuration import Configuration
from Logging.logger import Logger
from Display.Login import Login
from Display.MainGui import MainGui
import socket
from functions.Sendmessages import SendReceive


def main():

    sock = socket.socket()
    sock.connect((Configuration.ipAddress, Configuration.portNumber))
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    #CheckLog(sock, host_ip)
    Logger()
    #UserLocation().run()
    message = host_ip + "`Gui"
    SendReceive(sock, message).send()
    mess = SendReceive(sock, None).receive()
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
