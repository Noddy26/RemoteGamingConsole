from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Menu, YES, PhotoImage, BOTH
from PIL import Image, ImageDraw, ImageTk, ImageFont
import ctypes
import sys

from ClientGui.Configuration import Configuration
from ClientGui.DatbaseCheck import DatabaseCheck

from ClientGui.VideoWindow import VideoWindow
from ClientGui.gif_player import GifPlayer


class MainGui:

    def __init__(self, login_window, socket):
        if login_window is not None:
            login_window.destroy()
        self.socket = socket
        self.window = Tk()
        self.window.title("Gaming Server")
        self.image_file = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\Playstation-Wallpaper-20-1920x1080.jpg"
        self.play_gif = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\loading.gif"
        height, width = self._screen_size()
        self.window.geometry("%sx%s" % (height, width))

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

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def start_stream(self):

        self.gif = GifPlayer(self.window, self.play_gif).place(x=500, y=200)
        self.gif.pack()

        if Configuration.frames and Configuration.quality is not None:
            frames = str(Configuration.frames)
        else:
            frames = "30"
            Configuration.quality = "720x480"
        message = "StartStreamingServer," + Configuration.quality + "," + frames
        if DatabaseCheck(None, None, message, self.socket).start_Stream() is True:
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
        message = "Connection Terminate"
        if DatabaseCheck(None, None, message, self.socket).disconnect() is True:
            sys.exit(0)

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Do you want to quit?"):
            message = "Connection Terminate"
            DatabaseCheck(None, None, message, self.socket).disconnect()
            sys.exit(0)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
