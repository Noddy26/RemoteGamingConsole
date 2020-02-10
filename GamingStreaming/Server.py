import socket
import numpy as np
from GamingStreaming.ClientThread import ClientThread
from registerServer.Configuration import Configuration


class Server:

    def __init__(self):
        self.sock = socket.socket()
        self.host = Configuration.ipAddress
        self.port = 8080
        self.buffer = 1024

    def run(self):
        global threads
        try:
            tcpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpServer.bind((self.host, self.port))
            threads = []
            print('Server started!')
            print('Waiting for clients...')
            while True:
                tcpServer.listen(4)
                (conn, (ip, port)) = tcpServer.accept()
                newthread = ClientThread(ip, port, conn)
                newthread.start()
                threads.append(newthread)
        except():
            for t in threads:
                t.join()
            self.sock.close()


Server().run()
