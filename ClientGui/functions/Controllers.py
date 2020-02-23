from tkinter import messagebox
from threading import Thread
from inputs import devices, get_gamepad

from ClientGui.Logging.logger import Logger
from ClientGui.functions.Sendmessages import SendReceive


class ControllerControl(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        self.gameExit = False

    def run(self):
        try:
            Logger.info("Thread for controller started")
            while not self.gameExit:
                events = get_gamepad()
                for event in events:
                    if event.state is not 0:
                        SendReceive(self.socket, event.code + "-" + str(event.state)).send()
        except:
            Logger.error("Controller disconnected by user")

    def stop(self):
        Logger.info("Stopping Controller sent to ")
        self.gameExit = True
        self.join()

    @staticmethod
    def showController():
        if len(devices.gamepads) is not 0:
            for each in devices.gamepads:
                if each is not None:
                    if str(each).__contains__("Microsoft"):
                        control = "Xbox Controller"
                        Logger.info(control)
                        messagebox.showinfo(title="Controller Found", message=control + " found")
                        return True
        else:
            Logger.info("No controller Found")
            messagebox.showinfo(title="Controller", message="Controller not found")
            return False
