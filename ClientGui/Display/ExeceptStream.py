import ctypes
from tkinter import *
from threading import Thread
import io
import socket
import struct
from time import sleep
from PIL import Image, ImageTk
from variables.Configuration import Configuration


class ExpectStream(Thread):

    def __init__(self, window):
        Thread.__init__(self)
        sleep(5)
        self.window = window
        self.vidLabel = Label(self.window, anchor=NW)
        self.vidLabel.pack(expand=YES, fill=BOTH)
        self.client_socket = socket.socket()
        self.streamer = True
        print("waiting to except stream")

    def run(self):
        print("Starting")
        sleep(5)
        self.client_socket.connect((Configuration.ipAddress, 2005))
        Configuration.connection = self.client_socket.makefile('b')
        connection = Configuration.connection
        try:
            while self.streamer is True:
                main = False
                image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    print("break")
                    break

                image_stream = io.BytesIO()
                image_stream.write(connection.read(image_len))
                image_stream.seek(0)
                frame3 = Image.open(image_stream)
                self.img_copy = frame3.copy()
                image = ImageTk.PhotoImage(frame3)
                self.vidLabel.configure(image=image)
                self.vidLabel.image = image
                # if main is False:
                #     main = True
                #     self.vidLabel.bind('<Configure>', self._resize_image)
                self.vidLabel.place(x=0, y=0)
        finally:
            connection.close()

    def kill(self):
        self.streamer = False
        Configuration.connection.close()
        self.client_socket.shutdown(socket.SHUT_WR)
        self.client_socket.close()

    def _resize_image(self, event):
        #new_width, new_height = self._screen_size()
        new_width = 1370
        new_height = 740

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.vidLabel.configure(image=self.background_image)

    def _screen_size(self):
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
