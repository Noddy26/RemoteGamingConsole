from tkinter import messagebox
from threading import Thread
from inputs import devices, get_gamepad

from ClientGui.Logging.logger import Logger
from ClientGui.functions.Sendmessages import SendReceive


class ControllerControl(Thread):

    def __init__(self, socket):
        Thread.__init__(self)
        self.socket = socket
        SendReceive(self.socket, "ControllerOn").send()
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
            print("hello")
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
                        messagebox.showinfo(title="Controller Found", message=control)
                        return True
        else:
            Logger.info("No controller Found")
            messagebox.showinfo(title="Controller", message="Controller not found")
            return False

    def check(self, data):
        dictionary = {"ABS_HAT0Y_-1": "ABS_HAT0Y_1", "ABS_HAT0Y_1": "ABS_HAT0Y_2", "ABS_HAT0X_-1": "ABS_HAT0X_3",
                      "ABS_HAT0X_1": "ABS_HAT0X_4", "BTN_THUMBL_1": "BTN_THUMBL_5", "BTN_TL_1": "BTN_TL_6",
                      "BTN_START_1": "BTN_START_7", "home_button_1": "home_button_8", "BTN_SELECT_1": "BTN_SELECT_9",
                      "BTN_TR_1": "BTN_TR_10", "BTN_THUMBR_1": "BTN_THUMBR_11", "BTN_WEST_1": "BTN_WEST_12",
                      "BTN_NORTH_1": "BTN_NORTH_13", "BTN_EAST_1": "BTN_EAST_14", "BTN_SOUTH_1": "BTN_SOUTH_15"}

        if data in dictionary:
            data = dictionary[data]
            SendReceive(self.socket, data).send()
        else:
            other_data = str(data).split("_")
            changed_data = other_data[0] + other_data[1]
            if changed_data == "ABSZ":
                SendReceive(self.socket, "ABSZ_16").send()
            elif changed_data == "ABSRZ":
                SendReceive(self.socket, "ABSRZ_17").send()
            elif changed_data == "ABSX":
                SendReceive(self.socket, "ABSX_18_" + other_data[2]).send()
            elif changed_data == "ABSY":
                SendReceive(self.socket, "ABSY_19_" + other_data[2]).send()
            elif changed_data == "ABSRX":
                SendReceive(self.socket, "ABSRX20_" + other_data[2]).send()
            elif changed_data == "ABSRY":
                SendReceive(self.socket, "ABSRY20_" + other_data[2]).send()
