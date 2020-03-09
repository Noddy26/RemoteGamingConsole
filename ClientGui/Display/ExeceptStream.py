import struct
import socket
import pickle
import tkinter
from threading import Thread

import PIL
from PIL import Image, ImageTk
import tkinter as tki
import threading
import datetime
import imutils
import cv2
import os
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
            #height, width, no_channels = frame.shape
            canvas = tkinter.Canvas(self.window, width=1000, height=800)
            canvas.pack()
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
            canvas.place(x=0, y=0)
            #cv2.namedWindow("preview")
            #cv2.imshow('ImageWindow', image)
            #cv2.waitKey(1)

    def stop(self):
        print("hello")

    def _scale(self, image):
        width, height, channels = image.shape
        w = int(width * 2)
        h = int(height * 1.5)
        dim = (w, h)
        image_scaled = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        # cv.imshow('', image_scaled)
        # cv2.waitKey(0)
        return image_scaled