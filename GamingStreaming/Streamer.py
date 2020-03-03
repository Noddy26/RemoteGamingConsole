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
            tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpServer.bind((self.host, self.port))
            threads = []
            print('Stream Server started!')
            print('Waiting for the client...')
            while Configuration.server_running is True:
                tcpServer.listen(4)
                (conn, (ip, port)) = tcpServer.accept()
                newthread = VideoFeed(self.quality, self.frames, ip, port, conn)
                newthread.start()
                threads.append(newthread)
        except():
            for t in threads:
                t.join()
            self.sock.close()

    def stop(self):
        print("Stopping Stream Server")
        Configuration.server_running = False
        self.sock.close()
        for t in threads:
            t.join()
        self.sock.close()
