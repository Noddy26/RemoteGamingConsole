from threading import Thread
import subprocess
import socket
from ClientGui.variables.Configuration import Configuration


class ExpectStream(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.client_socket = socket.socket()
        self.client_socket.connect((Configuration.ipAddress, 2005))

    def play(self):
        connection = self.client_socket.makefile('wb')
        try:
            #cmdline = ['vlc', '--demux', 'h264', '-']
            cmdline = [r'"C:\Program Files\VideoLAN\VLC\vlc.exe"', '-fps', '25', '-cache', '1024', '-']
            self.player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
            while True:
                data = connection.read(1024)
                if not data:
                    break
                self.player.stdin.write(data)
        finally:
            connection.close()
            self.client_socket.close()
            self.player.terminate()

    def stop(self):
        print("hello")
