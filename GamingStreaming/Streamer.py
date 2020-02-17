import io
import struct
import time
import picamera
import socket
from threading import Thread

from registerServer.Configuration import Configuration


class Streamer(Thread):

    def __init__(self, frames, quality):
        Thread.__init__(self)
        Configuration.streaming = True
        self.host = Configuration.ipAddress
        self.port = Configuration.stream_portNumber
        self.frames = frames
        self.quality = quality

    def run(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            threads = []
            if Configuration.streaming == True:
                with picamera.PiCamera(resolution=self.quality, framerate=int(self.frames)) as hdmi_input:
                    hdmi_input.start_preview()
                    time.sleep(2)

                    stream = io.BytesIO()

                    for _ in hdmi_input.capture_continuous(stream, 'jpeg'):
                        self.socket.write(struct.pack('<L', stream.tell()))  # Write the length of the capture to the stream and flush toensure it actually gets sent
                        self.socket.flush()
                        stream.seek(0)
                        self.socket.write(stream.read())
                        if Configuration.streaming is False:
                            break
                        stream.seek(0)
                        stream.truncate()
                self.socket.write(struct.pack('<L', 0))
        finally:
            self.socket.close()

    def stop(self):
        print("Stopping stream")
        Configuration.streaming = False
        self.socket.close()
