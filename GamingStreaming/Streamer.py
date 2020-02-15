import base64
import cv2
import zmq

class Streamer:

    def __init__(self, frames, quality, socket):
        self.frames = frames
        self.quality = quality
        self.socket = socket


    def run(self):
        camera = cv2.VideoCapture(0)

        while True:
            try:
                grabbed, frame = camera.read()
                frame = cv2.resize(frame, (640, 480))
                encoded, buffer = cv2.imencode('.jpg', frame)
                jpg_as_text = base64.b64encode(buffer)
                self.socket.send(jpg_as_text)

            except KeyboardInterrupt:
                camera.release()
                cv2.destroyAllWindows()
                break
