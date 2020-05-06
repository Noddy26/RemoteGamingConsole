import socket
from multiprocessing.context import Process
from libs.GamingStreaming.videoFeed import VideoFeed


class Streamer(Process):

    def __init__(self, quality, frames):
        super().__init__()
        self.quality = quality
        self.frames = frames
        self.sock = socket.socket()
        self.host = "192.168.1.13"
        self.port = 2005
        self.buffer = 1024
        self.server_running = True
        global threads, newthread
        try:
            self.streamServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.streamServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.streamServer.bind((self.host, self.port))
            threads = []
            print('Stream Server started!')
            print('Waiting for the client...')
            while self.server_running is True:
                self.streamServer.listen(4)
                try:
                    (connection, (ip, port)) = self.streamServer.accept()
                    newthread = VideoFeed(self.quality, self.frames, ip, port, connection)
                except socket.error as serr:
                    print(serr)
                newthread.start()
                threads.append(newthread)
        except():
            for t in threads:
                t.Join()
            self.sock.close()

    def kill(self):
        print("Stopping Stream Server")
        self.server_running = False
        self.streamServer.shutdown(socket.SHUT_RDWR)
        self.streamServer.close()
