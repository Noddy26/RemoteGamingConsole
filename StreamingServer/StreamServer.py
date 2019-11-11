import socket
import struct
import numpy as np
import cv2

host = "192.168.0.100"
port = 6000

Sever = socket.socket()
Sever.bind((host, port))

Sever.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
Sever.listen(0)
print("Waiting for Gaming Server connection...")

Client = Sever.accept()[0]
StreamFile = Client.makefile("rb")
print("Connection made with Gaming Server")
Sever.settimeout(30)
numOfBytes = struct.calcsize("<L")
try:
    while(True):
        Sever.setblocking(False)
        imageLength = struct.unpack("<L", StreamFile.read(numOfBytes))[0]
        if imageLength == 0:
            break

        nparr = np.frombuffer(StreamFile.read(imageLength), np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        cv2.imshow('RC Car Video stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    StreamFile.close()
    Sever.close()
    cv2.destroyAllWindows()
    print("Server - Camera connection closed")
