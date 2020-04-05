import socket
from threading import Thread
from Server_code.GamingStreaming.ClientThread import ClientThread
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
            threads = []
            Configuration.Gui_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock = Configuration.Gui_Socket
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            print('Server started!')
            print('Waiting for clients...')
            while Configuration.server_running is True:
                self.sock.listen(0)
                (conn, (ip, port)) = self.sock.accept()
                newthread = ClientThread(ip, port, conn)
                newthread.start()
                print("starting")
                threads.append(newthread)
                for thread in threads:
                    if thread.is_alive():
                        pass
                    else:
                        thread.join()
        finally:
            for t in threads:
                t.join()
            self.sock.close()
            return

    def stop(self):
        print("Stopping Server")
        Configuration.server_running = False
        Configuration.Gui_Socket.shutdown(socket.SHUT_RDWR)
        Configuration.Gui_Socket.close()
