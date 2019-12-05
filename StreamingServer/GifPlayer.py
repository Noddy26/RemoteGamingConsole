from tkinter import *
from PIL import Image, ImageTk

class GifPlayer(Label):

    def __init__(self, frame, filename):
        gif = Image.open(filename)
        seq = []
        try:
            while 1:
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

        Label.__init__(self, frame, image=self.frames[0])

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

