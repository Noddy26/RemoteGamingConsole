from threading import Thread
import io
import struct
import socket
import numpy as np
import cv2

from ClientGui.variables.Configuration import Configuration


class ExpectStream(Thread):

    def __init__(self):
        Thread.__init__(self)
        print("waiting to except stream")
        self.client_socket = socket.socket()
        self.client_socket.connect((Configuration.ipAddress, 2005))

    def play(self):
        connection = self.client_socket.makefile('wb')
        try:
            while True:
                image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break
                image_stream = io.BytesIO()
                image_stream.write(connection.read(image_len))
                image_stream.seek(0)

                data = np.fromstring(image_stream.getvalue(), dtype=np.uint8)
                imagedisp = cv2.imdecode(data, 1)

                cv2.imshow("Frame", imagedisp)
        finally:
            connection.close()
            self.client_socket.close()


    def stop(self):
        print("hello")
