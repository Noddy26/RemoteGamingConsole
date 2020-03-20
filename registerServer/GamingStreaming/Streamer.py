import socket
from threading import Thread
from Configuration import Configuration

from GamingStreaming.videoFeed import VideoFeed


class Streamer(Thread):

    def __init__(self, quality, frames):
        print("coming")
        Thread.__init__(self)
        self.quality = quality
        self.frames = frames
        self.sock = socket.socket()
        self.host = Configuration.ipAddress
        self.port = 2005
        self.buffer = 1024
        Configuration.server_running = True

    def run(self):
        global threads, newthread
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
                (connection, (ip, port)) = self.streamServer.accept()
                newthread = VideoFeed(self.quality, self.frames, ip, port, connection)
                newthread.start()
                threads.append(newthread)
        except():
            for t in threads:
                t.Join()
            self.sock.close()

    def kill(self):
        print("Stopping Stream Server")
        Configuration.server_running = False
        newthread.stop()
        Configuration.Stream_Socket.shutdown(socket.SHUT_RDWR)
        Configuration.Stream_Socket.close()
