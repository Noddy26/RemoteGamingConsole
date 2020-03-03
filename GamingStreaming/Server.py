import socket
from threading import Thread
from GamingStreaming.ClientThread import ClientThread
from Configuration import Configuration


class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.sock = socket.socket()
        self.host = Configuration.ipAddress
        self.port = Configuration.Serverport
        self.buffer = 1024
        Configuration.server_running = True

    def run(self):
        global threads
        try:
            tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpServer.bind((self.host, self.port))
            threads = []
            print('Server started!')
            print('Waiting for clients...')
            while Configuration.server_running is True:
                tcpServer.listen(4)
                (conn, (ip, port)) = tcpServer.accept()
                newthread = ClientThread(ip, port, conn)
                newthread.start()
                print("starting")
                threads.append(newthread)
        except():
            for t in threads:
                t.join()
            self.sock.close()

    def stop(self):
        print("Stopping Server")
        Configuration.server_running = False
        self.sock.close()
