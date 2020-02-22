import time
import picamera
import socket
from threading import Thread

from Configuration.Configuartion import Configuration


class Streamer(Thread):

    def __init__(self, frames, quality):
        Thread.__init__(self)
        Configuration.streaming_has_started = True
        self.host = Configuration.ipAddress
        self.port = Configuration.stream_portNumber
        self.frames = frames
        self.quality = quality

    def run(self):
        global hdmi_input
        try:
            print("Turning on hdmi input")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            while Configuration.streaming_has_started == True:
                with picamera.PiCamera(resolution=self.quality, framerate=int(self.frames)) as hdmi_input:
                    Configuration.streamStarted = True
                    hdmi_input.start_preview()
                    time.sleep(2)
                    hdmi_input.start_recording(self.socket, format='h264')
        finally:
            print("Stream finished or Error occurred")
            Configuration.streaming_has_started = False
            Configuration.streamStarted = False
            self.socket.close()


    def stop(self):
        print("Stopping stream")
        Configuration.streaming_has_started = False
        self.socket.close()
