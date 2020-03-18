import io
import struct
import time
import picamera
import cv2
from threading import Thread


class VideoFeed(Thread):

    def __init__(self, quality, frames, ip, port, conn):
        Thread.__init__(self)
        print("Starting stream")
        self.connection = conn.makefile('wb')
        self.new = quality.split("x")
        self.frames = str(frames).replace("fps", "")
        self.running = True

        print("New Streaming Thread started for " + ip + ":" + str(port))

    def run(self):
        try:
            first = self.new[0]
            second = self.new[1]
            with picamera.PiCamera() as camera:
                camera.resolution = (int(first), int(second))
                camera.framerate = int(self.frames)
                camera.start_preview()
                time.sleep(2)

                stream = io.BytesIO()
                for _ in camera.capture_continuous(stream, 'jpeg'):
                    self.connection.write(struct.pack('<L', stream.tell()))
                    self.connection.flush()
                    stream.seek(0)
                    self.connection.write(stream.read())
                    if self.running is True:
                        break
                    stream.seek(0)
                    stream.truncate()
            self.connection.write(struct.pack('<L', 0))
        finally:
            self.connection.close()

    def stop(self):
        print("Stopping stream socket")
        self.running = False
        self.join()
