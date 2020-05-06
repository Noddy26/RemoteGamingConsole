from functions.Sendmessages import SendReceive
from functions.Upgrade import Upgrade
from variables.Configuration import Configuration
from functions.Controllers import ControllerControl
from functions.DatbaseCheck import DatabaseCheck
from Display.ExeceptStream import ExpectStream
from Logging.logger import Logger
from Display.VideoWindow import VideoWindow
from Display.gif_player import GifPlayer
import multiprocessing
from tkinter import Tk, Label, messagebox, Menu, YES, BOTH
from PIL import Image, ImageTk
import ctypes
import os, time
import webbrowser

class MainGui:

    def __init__(self, login_window, socket):
        Configuration.start_time = time.time()
        if login_window is not None:
            login_window.destroy()
        self.socket = socket
        self.window = Tk()
        self.window.title("Gaming Server")
        self.image_file = r"Pictures\Playstation-Wallpaper-20-1920x1080.jpg"
        self.play_gif = r"Pictures\Fmh8EMk.gif"
        self.height, self.width = self._screen_size()
        self.window.geometry("%sx%s" % (self.height - 40, self.width - 70))

    def run(self):
        Logger.info("Starting Main Gui")
        self.image = Image.open(self.image_file)
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self.window, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        menu = Menu(self.window)
        self.window.config(menu=menu)

        self.system = Menu(menu, tearoff=False)
        self.configure = Menu(menu, tearoff=False)
        help = Menu(menu, tearoff=False)

        self.system.add_command(label="Start Stream", command=self.start_stream)
        self.system.add_command(label="Stop Stream", command=self.stop_stream)
        self.system.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="System", menu=self.system)

        self.configure.add_command(label="Detect Controller", command=self.controller)
        self.configure.add_command(label="Enable Two Player", command=self.two_player)
        self.configure.add_command(label="Audio", command=self.audio)
        self.configure.add_command(label="Video", command=self.video)
        menu.add_cascade(label="Configure", menu=self.configure)

        help.add_command(label="about", command=self.about)
        menu.add_cascade(label="Help", menu=help)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()
        SendReceive(self.socket, "Guiversion")
        version = SendReceive(self.socket, None).receive()
        if float(version) > float(Configuration.version):
            Upgrade()

    def start_stream(self):
        global thread
        self.p1 = multiprocessing.Process(target=GifPlayer(self.window, self.play_gif).place(x=-250, y=-140))
        self.p1.start()


        if Configuration.frames and Configuration.quality is not None:
            frames = str(Configuration.frames)
        else:
            frames = "30"
            Configuration.quality = "1280x720"
        message = "StartStreamingServer," + Configuration.quality + "," + frames
        if DatabaseCheck(None, None, message, self.socket).start_Stream() is True:
            Configuration.stream_started = True
            thread = ExpectStream(self.window)
            thread.start()
        else:
            if messagebox.askokcancel("Server Error", "Do you want to quit?"):
                message = "Connection Terminate"
                DatabaseCheck(None, None, message, self.socket).disconnect()
                os._exit(0)

    def stop_stream(self):
        Logger.info("stopping stream")
        if Configuration.stream_started is True:
            Configuration.stream_started = False
            SendReceive(self.socket, "Stop").send()
            thread.kill()
            thread.join()
            try:
                ExpectStream(None).vidLabel.destroy()
            except Exception as e:
                Logger.error(e)
            self.p1.kill()
            self.p1.join()

            GifPlayer(None, None).stop()
            Logger.info("stopping stream")

        else:
            messagebox.showerror("Stream", "Stream hasn't Started")

    def controller(self):
        if Configuration.stream_started is True:
            Logger.info("Controller")
            if ControllerControl.showController() is True:
                ControllerThread = ControllerControl(self.socket)
                ControllerThread.start()
                Logger.info("Controller Thread working")
            else:
                return
        else:
            messagebox.showerror("Stream", "Start Stream First")

    def audio(self):
        Logger.info("Audio")

    def two_player(self):
        Logger.info("Two Player enabled")
        self.configure.delete(1, 1)
        self.configure.add_command(label="Disable Two Player", command=self.disable_two_player)
        SendReceive(self.socket, "Enable/twoPlayer").send()
        messagebox.askokcancel("Stream", "Two Player enabled")

    def disable_two_player(self):
        Logger.info("Two Player disabled")
        self.configure.delete(1, 3)
        self.configure.add_command(label="Enable Two Player", command=self.two_player)
        SendReceive(self.socket, "disable/twoPlayer").send()
        messagebox.askokcancel("Stream", "Two Player disabled")

    def video(self):
        if Configuration.stream_started is False:
            Logger.info("Video")
            VideoWindow(self.window).run()
        else:
            messagebox.showerror("Stream", "Stream has Started, Stop stream and change resolution")

    def about(self):
        Logger.info("About")
        url = 'http://' + Configuration.ipAddress + ':' + str(Configuration.port_for_website) + '/index4'
        webbrowser.open_new(url)

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
            if os.path.exists("Logging/Logs/debug_" + Configuration.Username + ".log"):
                SendReceive(self.socket, None).sendfile()
            os._exit(0)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
