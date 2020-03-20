from tkinter import *
from PIL import Image, ImageTk
from threading import Thread


class GifPlayer(Label):

    def __init__(self, frames, filename):
        self.running = True
        gif = Image.open(filename)
        seq = []
        try:
            while self.running:
                seq.append(gif.copy())
                gif.seek(len(seq))
        except EOFError:
            pass

        try:
            self.delay = gif.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, frames, image=self.frames[-1])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))
        self.index = 0
        self.cancel = self.after(self.delay, self.run)

    def run(self):
        self.config(image=self.frames[self.index])
        self.index += 1
        if self.index == len(self.frames):
            self.index = 0
        self.cancel = self.after(self.delay, self.run)

    def stop(self):
        print("stopping")
        self.running = False
        self.pack_forget()
