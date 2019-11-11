from tkinter import Menu, Tk, Label, messagebox
from tkinter import Frame
from tkinter import Canvas
from tkinter import BOTTOM
from tkinter import TOP
from tkinter import Button
from PIL import Image, ImageTk
import socket
import struct
import numpy as np
import cv2
from multiprocessing import Process
import queue

from StreamingServer.GifPlayer import GifPlayer


class videoGUI:

    def __init__(self, window, window_title):

        self.host = "192.168.0.101"
        self.port = 6000
        self.queue = queue.Queue()

        menubar = Menu(window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Stream options", command="do nothing")
        filemenu.add_command(label="Connect Controller", command="do nothing")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="Options", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.image = r"C:\Users\\neilm\PycharmProjects\GamingGui\StreamingServer\Static\giphy.gif"

        window.config(menu=menubar)
        self.window = window
        self.window.title(window_title)

        top_frame = Frame(self.window)
        top_frame.pack(side=TOP, pady=5)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=BOTTOM, pady=5)

        self.pause = False

        #self.canvas = Canvas(top_frame)
        #self.canvas.pack()



        self.btn_select = Button(bottom_frame, text="Start streaming", width=15, command=self.loading)
        self.btn_select.grid(row=0, column=0)
        self.btn_play = Button(bottom_frame, text="Expand", width=15, command=self.expandwindow)
        self.btn_play.grid(row=0, column=1)
        self.btn_pause = Button(bottom_frame, text="Pause", width=15, command=self.pause_video)
        self.btn_pause.grid(row=0, column=2)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.delay = 15
        self.window.mainloop()

    def loading(self):
        print("Loading video from server")
        gif = GifPlayer(self.window, r"C:\Users\neilm\PycharmProjects\GamingGui\StreamingServer\Dynamic\loading.gif")
        gif.pack()
        self.queue = Process(target=self.startThread())
        self.queue.start()
        self.window.mainloop()

        def stop_it():
            gif.after_cancel(gif.cancel)


    def startThread(self):
        thread1 = Process(target=self.open_Stream())
        thread1.start()
        thread1.join()


    def open_Stream(self):

        print(self.host)
        Sever = socket.socket()
        Sever.bind((self.host, self.port))

        Sever.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        Sever.listen(0)
        print("Waiting for Gaming Server connection...")

        Client = Sever.accept()[0]
        camFile = Client.makefile("rb")
        print("Connection made with Gaming Server")
        Sever.settimeout(30)
        numOfBytes = struct.calcsize("<L")
        try:
            while (True):
                Sever.setblocking(False)
                imageLength = struct.unpack("<L", camFile.read(numOfBytes))[0]
                if imageLength == 0:
                    break
                nparr = np.frombuffer(camFile.read(imageLength), np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                cv2.imshow('Gaming Stream', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            camFile.close()
            Sever.close()
            cv2.destroyAllWindows()
            print("Server - Camera connection closed")


    def expandwindow(self):
        self.window.geometry("1350x670-5-28")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # self.image = self.img_copy.resize((screen_width, screen_height))
        # self.background_image = ImageTk.PhotoImage(self.image)
        # self.background.configure(image=self.background_image)


    def pause_video(self):
        self.pause = True


    def on_close(self):
        close = messagebox.askokcancel("Close", "Would you like to close the program?")
        if close:
            self.window.destroy()


    def getIp(self):
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        return IP

videoGUI(Tk(), "Gaming Server")