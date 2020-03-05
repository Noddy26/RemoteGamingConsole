import pickle
import struct
import cv2
from threading import Thread
from Configuration import Configuration


class VideoFeed(Thread):

    def __init__(self, quality, frames, ip, port, conn):
        Thread.__init__(self)
        print("Starting stream")
        self.connection = conn
        new = quality.split("x")
        self.running = True
        self.first = new[0]
        self.second = new[1]
        print("New Streaming Thread started for " + ip + ":" + str(port))
        try:
            self.hdmi = cv2.VideoCapture(0)
            self.hdmi.set(3, self.first)
            self.hdmi.set(4, self.second)
            self.hdmi.set(5, frames)
            self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            self.img_counter = 0
        except:
            self.hdmi.release()
            self.connection.close()

    def run(self):
        while self.running:
            try:
                ret, frame = self.hdmi.read()
                result, frame = cv2.imencode('.jpg', frame, self.encode_param)
                data = pickle.dumps(frame, 0)
                size = len(data)
                self.connection.sendall(struct.pack(">L", size) + data)
                self.img_counter += 1
            except:
                self.hdmi.release()
                self.connection.close()
                return False

    def stop(self):
        print("Stopping stream socket")
        self.running = False
        self.join()
