import socket
from threading import Thread
from GamingStreaming.ClientThread import ClientThread
from Configuration import Configuration


class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.host = Configuration.ipAddress
        self.port = Configuration.Serverport
        self.buffer = 1024
        Configuration.server_running = True

    def run(self):
        global threads
        try:
            Configuration.Gui_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock = Configuration.Gui_Socket
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            print('Server started!')
            print('Waiting for clients...')
            while True:
                if Configuration.server_running is False:
                    break
                self.sock.listen(0)
                (conn, (ip, port)) = self.sock.accept()
                newthread = ClientThread(ip, port, conn)
                newthread.start()
                newthread.setDaemon(True)
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
