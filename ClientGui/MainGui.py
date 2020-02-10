from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Menu, YES
from PIL import Image, ImageDraw, ImageTk, ImageFont
import ctypes
import sys

from ClientGui.Configuration import Configuration
from ClientGui.DatbaseCheck import DatabaseCheck
from ClientGui.VideoWindow import VideoWindow


class MainGui:

    def __init__(self, login_window):
        if login_window is not None:
            login_window.destroy()
        self.window = Tk()
        self.window.title("Gaming Server")
        self.image_file = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\Playstation-Wallpaper-20-1920x1080.jpg"
        self.play_gif = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\22.gif"
        height, width = self._screen_size()
        self.window.geometry("%sx%s" % (height, width))

    def run(self):
        print("Starting Main Gui")
        image = Image.open(self.image_file)
        gif = Image.open(self.play_gif)

        draw = ImageDraw.Draw(image)

        photoimage = ImageTk.PhotoImage(image)
        self.gifimage = ImageTk.PhotoImage(gif)
        Label(self.window, image=photoimage).place(x=0, y=0)

        menu = Menu(self.window)
        self.window.config(menu=menu)

        system = Menu(menu)
        configure = Menu(menu)
        help = Menu(menu)


        system.add_command(label="Start Stream", command=self.start_stream)
        system.add_command(label="Stop Stream", command=self.stop_stream)
        system.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="System", menu=system)

        configure.add_command(label="Controller", command=self.controller)
        configure.add_command(label="Audio", command=self.audio)
        configure.add_command(label="Video", command=self.video)
        menu.add_cascade(label="Configure", menu=configure)

        help.add_command(label="about", command=self.about)
        menu.add_cascade(label="Help", menu=help)


        self.window.mainloop()

    def start_stream(self):
        Label(self.window, image=self.gifimage).place(x=0, y=0)
        if Configuration.frames and Configuration.quality is not None:
            frames = str(Configuration.frames)
        else:
            frames = "25"
            Configuration.quality = "1280x720"
        message = "StartStreamingServer_" + Configuration.quality + "_" + frames
        if DatabaseCheck(None, None, message).start_Stream() is True:
            print("well done")

    def stop_stream(self):
        print("stopping stream")

    def controller(self):
        print("Controller")

    def audio(self):
        print("Audio")

    def video(self):
        print("Video")
        VideoWindow(self.window).run()

        #self.window.mainloop()

    def about(self):
        print("About")

    def _screen_size(self):
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def exit(self):
        sys.exit(0)
