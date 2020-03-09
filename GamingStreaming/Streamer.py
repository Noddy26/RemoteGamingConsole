import picamera
import io
import subprocess
import socket
from threading import Thread
from Configuration import Configuration
from GamingStreaming.videoFeed import VideoFeed


class Streamer(Thread):

    def __init__(self, quality, frames):
        Thread.__init__(self)
        self.quality = quality
        self.frames = frames
        self.sock = socket.socket()
        self.host = Configuration.ipAddress
        self.port = 2005
        self.buffer = 1024
        Configuration.server_running = True

    def run(self):
        global threads
        try:
            Configuration.Gui_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.streamServer = Configuration.Gui_Socket
            self.streamServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.streamServer.bind((self.host, self.port))
            threads = []
            print('Stream Server started!')
            print('Waiting for the client...')
            while Configuration.server_running is True:
                self.streamServer.listen(4)
                (conn, (ip, port)) = self.streamServer.accept()
                newthread = VideoFeed(self.quality, self.frames, ip, port, conn)
                newthread.start()
                threads.append(newthread)
        except():
            for t in threads:
                t.join()
            self.streamServer.close()

    def stop(self):
        print("Stopping Stream Server")
        Configuration.server_running = False
        for t in threads:
            t.stop()
        Configuration.Stream_Socket.shutdown(socket.SHUT_RDWR)
        Configuration.Stream_Socket.close()
