import picamera
import io
import subprocess
import socket
import struct
from threading import Thread
from Configuration import Configuration


class VideoFeed(Thread):

    def __init__(self, quality, frames, ip, port, conn):
        Thread.__init__(self)
        print("Starting stream")
        self.connection = conn
        new = quality.split("x")
        first = new[0]
        second = new[1]
        print("New Streaming Thread started for " + ip + ":" + str(port))
        self.camera = picamera.PiCamera(resolution=(int(first), int(second)), framerate=frames)

    def run(self):
        global hdmi_input
        while True:
            print("Turning on hdmi input")
            try:
                stream = io.BytesIO()
                for _ in self.camera.capture_continuous(stream, 'jpeg'):
                    self.connection.write(struct.pack('<L', stream.tell()))
                    self.connection.flush()
                    stream.seek(0)
                    self.connection.write(stream.read())
                    stream.seek(0)
                    stream.truncate()
                # gst - launch - 1.0
                # filesrc
                # location = test.ogg ! oggdemux
                # name = demuxer
                # demuxer. ! queue ! vorbisdec ! audioconvert ! audioresample ! autoaudiosink
                # demuxer. ! queue ! theoradec ! autovideosink
                # audio = subprocess.Popen(['gst-launch-1.0', '-v', 'fdsrc', '!', ''])
            finally:
                print("Stopping stream")
                self.connection.close()
                self.camera.stop_recording()
                Configuration.streaming_has_started = False
                return False
