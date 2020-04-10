from ClientGui.functions.Sendmessages import SendReceive
from ClientGui.variables.Configuration import Configuration
from ClientGui.functions.Controllers import ControllerControl
from ClientGui.functions.DatbaseCheck import DatabaseCheck
from ClientGui.Display.ExeceptStream import ExpectStream
from ClientGui.Logging.logger import Logger
from ClientGui.Display.VideoWindow import VideoWindow
from ClientGui.Display.gif_player import GifPlayer
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

        self.system = Menu(menu, tearoff=False)
        configure = Menu(menu, tearoff=False)
        help = Menu(menu, tearoff=False)

        self.system.add_command(label="Start Stream", command=self.start_stream)
        self.system.add_command(label="Stop Stream", command=self.stop_stream)
        self.system.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="System", menu=self.system)

        configure.add_command(label="Detect Controller", command=self.controller)
        configure.add_command(label="Enable Two Player", command=self.two_player)
        configure.add_command(label="Audio", command=self.audio)
        configure.add_command(label="Video", command=self.video)
        menu.add_cascade(label="Configure", menu=configure)

        help.add_command(label="about", command=self.about)
        menu.add_cascade(label="Help", menu=help)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

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
            # TODO: GET STREAM
        else:
            if messagebox.askokcancel("Server Error", "Do you want to quit?"):
                message = "Connection Terminate"
                DatabaseCheck(None, None, message, self.socket).disconnect()
                os._exit(0)

    def stop_stream(self):
        print("stopping stream")
        if Configuration.stream_started is True:
            Configuration.stream_started = False
            SendReceive(self.socket, "Stop").send()
            thread.kill()
            thread.join()
            try:
                ExpectStream(None).vidLabel.destroy()
            except Exception as e:
                print(e)
            self.p1.join()
            self.p1.kill()
            #GifPlayer(None, None).stop()
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
        print("welcome")

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
