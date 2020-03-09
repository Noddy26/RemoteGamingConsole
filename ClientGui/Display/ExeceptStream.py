import struct
import socket
import pickle
from tkinter import *
from threading import Thread

from PIL import Image, ImageTk
import cv2

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
        buffer = b''
        payload_size = struct.calcsize("<L")
        vidLabel = Label(self.window, anchor=NW)
        vidLabel.pack(expand=YES, fill=BOTH)
        while True:
            while len(buffer) < payload_size:
                buffer += self.client_socket.recv(4096)
            frame_size = buffer[:payload_size]
            buffer = buffer[payload_size:]
            pic_size = struct.unpack(">L", frame_size)[0]
            while len(buffer) < pic_size:
                buffer += self.client_socket.recv(4096)
            frame_data = buffer[:pic_size]
            buffer = buffer[pic_size:]

            frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame3 = Image.fromarray(frame2)
            frame4 = ImageTk.PhotoImage(frame3)
            vidLabel.configure(image=frame4)
            vidLabel.image = frame4
            vidLabel.place(x=0, y=0)

    def stop(self):
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

