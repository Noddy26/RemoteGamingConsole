import socket
import struct
import numpy as np
import cv2

class StreamServer:

    def __init__(self):
        host = "192.168.22.1"
        port = 2

        self.Server = socket.socket()
        self.Server.bind((host, port))

        self.Server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.Server.listen(0)
        print("Waiting for Gaming Server connection...")

        Client = self.Server.accept()[0]
        self.StreamFile = Client.makefile("rb")
        print("Connection made with Gaming Server")
        self.Server.settimeout(30)
        self.numOfBytes = struct.calcsize("<L")

    def run(self):
        try:
            while(True):
                self.Server.setblocking(False)
                imageLength = struct.unpack("<L", self.StreamFile.read(self.numOfBytes))[0]
                if imageLength == 0:
                    break

                nparr = np.frombuffer(self.StreamFile.read(imageLength), np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                cv2.imshow('Gaming Server', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            self.StreamFile.cloLeftse()
            self.Server.close()
            cv2.destroyAllWindows()
            print("Server - Camera connection closed")
