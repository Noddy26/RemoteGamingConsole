from tkinter import *
from threading import Thread
import io
import socket
import struct
from PIL import Image, ImageTk

from ClientGui.variables.Configuration import Configuration


class ExpectStream(Thread):

    def __init__(self, window):
        Thread.__init__(self)
        self.window = window
        print("waiting to except stream")
        self.client_socket = socket.socket()
        self.client_socket.connect((Configuration.ipAddress, 2005))

    def run(self):
        print("Starting")
        connection = self.client_socket.makefile('b')
        self.vidLabel = Label(self.window, anchor=NW)
        self.vidLabel.pack(expand=YES, fill=BOTH)
        try:
            while True:
                image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break
                image_stream = io.BytesIO()
                image_stream.write(connection.read(image_len))
                image_stream.seek(0)
                frame3 = Image.open(image_stream)
                image = ImageTk.PhotoImage(frame3)
                self.vidLabel.configure(image=image)
                self.vidLabel.image = image
                self.vidLabel.place(x=0, y=0)
        finally:
            connection.close()

    def stop(self):
        self.vidLabel.destroy()
        self.join()
        print("hello")

    def _scale(self, image):
        width, height, channels = image.shape
        w = int(width * 3)
        h = int(height * 1.2)
        dim = (w, h)
        image_scaled = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        # cv.imshow('', image_scaled)
        # cv2.waitKey(0)
        return image_scaled

