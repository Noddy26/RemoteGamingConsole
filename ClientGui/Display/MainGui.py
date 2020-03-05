import multiprocessing
from tkinter import Tk, Label, messagebox, Menu, YES, BOTH
from PIL import Image, ImageTk
import ctypes
import os

from ClientGui.functions.Sendmessages import SendReceive
from ClientGui.variables.Configuration import Configuration
from ClientGui.functions.Controllers import ControllerControl
from ClientGui.functions.DatbaseCheck import DatabaseCheck
from ClientGui.Display.ExeceptStream import ExpectStream
from ClientGui.Logging.logger import Logger
from ClientGui.Display.VideoWindow import VideoWindow
from ClientGui.Display.gif_player import GifPlayer


class MainGui:

    def __init__(self, login_window, socket):
        if login_window is not None:
            login_window.destroy()
        self.socket = socket
        self.window = Tk()
        self.window.title("Gaming Server")
        self.image_file = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\Playstation-Wallpaper-20-1920x1080.jpg"
        self.play_gif = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\Fmh8EMk.gif"
        self.height, self.width = self._screen_size()
        self.window.geometry("%sx%s" % (self.height, self.width))

    def run(self):
        print("Starting Main Gui")
        self.image = Image.open(self.image_file)
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self.window, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        menu = Menu(self.window)
        self.window.config(menu=menu)

        self.system = Menu(menu)
        configure = Menu(menu)
        help = Menu(menu)

        self.system.add_command(label="Start Stream", command=self.start_stream)
        self.system.add_command(label="Stop Stream", command=self.stop_stream)
        self.system.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="System", menu=self.system)

        configure.add_command(label="Detect Controller", command=self.controller)
        configure.add_command(label="Audio", command=self.audio)
        configure.add_command(label="Video", command=self.video)
        menu.add_cascade(label="Configure", menu=configure)

        help.add_command(label="about", command=self.about)
        menu.add_cascade(label="Help", menu=help)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def start_stream(self):

        p1 = multiprocessing.Process(target=GifPlayer(self.window, self.play_gif).place(x=-250, y=-140))
        p1.start()
        print("passing by process")


        if Configuration.frames and Configuration.quality is not None:
            frames = str(Configuration.frames)
        else:
            frames = "30"
            Configuration.quality = "720x480"
        message = "StartStreamingServer," + Configuration.quality + "," + frames
        if DatabaseCheck(None, None, message, self.socket).start_Stream() is True:
            thread = ExpectStream(self.window)
            thread.start()
            # TODO: GET STREAM
        else:
            if messagebox.askokcancel("Server Error", "Do you want to quit?"):
                message = "Connection Terminate"
                DatabaseCheck(None, None, message, self.socket).disconnect()
                os._exit(0)


    def stop_stream(self):
        GifPlayer(self.window, self.play_gif).destroy()
        Logger.info("stopping stream")

    def controller(self):
        Logger.info("Controller")
        if ControllerControl.showController() is True:
            print("Found")
            ControllerThread = ControllerControl(self.socket)
            ControllerThread.start()
            Logger.info("Controller Thread working")
        else:
            return

    def audio(self):
        Logger.info("Audio")

    def video(self):
        Logger.info("Video")
        VideoWindow(self.window).run()

    def about(self):
        Logger.info("About")
        #TODO: Make a class to open a file in this executable

    def _screen_size(self):
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def exit(self):
        message = "Connection Terminate"
        Logger.info("Exiting gui")
        DatabaseCheck(None, None, message, self.socket).disconnect()
        if os.path.exists("ClientGui/Logging/debug_" + Configuration.Username + ".log"):
            SendReceive(self.socket, None).sendfile()
        os._exit(0)

    def on_closing(self):
        Logger.info("Exiting gui")
        if messagebox.askokcancel("Exit", "Do you want to quit?"):
            message = "Connection Terminate"
            DatabaseCheck(None, None, message, self.socket).disconnect()
            print(os.path.exists("Logging/Logs/debug_" + Configuration.Username + ".log"))
            if os.path.exists("Logging/Logs/debug_" + Configuration.Username + ".log"):
                SendReceive(self.socket, None).sendfile()
            os._exit(0)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
