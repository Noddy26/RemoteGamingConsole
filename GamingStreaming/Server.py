import socket
from GamingStreaming.ClientThread import ClientThread
from registerServer.Configuration import Configuration


class Server():

    def __init__(self):
        self.sock = socket.socket()
        self.host = "192.168.22.1"
        self.port = 2003
        self.buffer = 1024
        Configuration.running = True

    def run(self):
        global threads
        try:
            tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tcpServer.bind((self.host, self.port))
            threads = []
            print('Server started!')
            print('Waiting for clients...')
            while Configuration.running:
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
        Configuration.running = False
        socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM).connect((self.host, self.port))
        self.sock.close()

Server().run()