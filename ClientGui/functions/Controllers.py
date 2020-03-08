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
                        data = event.code + "_" + str(event.state)
                        self.check(data)

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
                        control = "Xbox Controller Detected"
                        Logger.info(control)
                        messagebox.showinfo(title="Controller Found", message=control + " found")
                        return True
        else:
            Logger.info("No controller Found")
            messagebox.showinfo(title="Controller", message="Controller not found")
            return False

    def check(self, data):
        dictionary = {"ABS_HAT0Y_-1": 1, "ABS_HAT0Y_1": 2, "ABS_HAT0X_-1": 3, "ABS_HAT0X_1": 4, "BTN_THUMBL_1": 5,
                      "BTN_TL_1": 6, "BTN_START_1": 7, "home_button_1": 8, "BTN_SELECT_1": 9, "BTN_TR_1": 10,
                      "BTN_THUMBR_1": 11, "BTN_WEST_1": 12, "BTN_NORTH_1": 13, "BTN_EAST_1": 14, "BTN_SOUTH_1": 15}

        if data in dictionary:
            data = dictionary[data]
            SendReceive(self.socket, data).send()
