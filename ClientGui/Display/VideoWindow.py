from tkinter import Toplevel, IntVar, Button, Checkbutton, Label, DISABLED, NORMAL
from tkinter import ttk

from ClientGui.variables.Configuration import Configuration
from ClientGui.Logging.logger import Logger


class VideoWindow:

    def __init__(self, window):
        Logger.info("Opened video window")
        self.window = window
        self.sub = Toplevel(self.window)
        self.radioVar1 = IntVar(value=0)
        self.radioVar2 = IntVar(value=0)
        self.radioVar3 = IntVar(value=0)

        self.radio1 = Checkbutton(self.sub, text="1020p", onvalue=1, offvalue=0,
                                  variable=self.radioVar1, command=self.hd)
        self.list1 = ttk.Combobox(self.sub, values=["15fps", "30fps", "25fps"])

        self.radio2 = Checkbutton(self.sub, text="720p", onvalue=1, offvalue=0,
                                  variable=self.radioVar2, command=self.hd_ready)
        self.list2 = ttk.Combobox(self.sub, values=["25fps", "30fps", "60fps"])

        self.radio3 = Checkbutton(self.sub, text="480p", onvalue=1, offvalue=0,
                                  variable=self.radioVar3, command=self.standard)
        self.list3 = ttk.Combobox(self.sub, values=["30fps", "60fps", "90fps"])

        self.button = Button(self.sub, text="Apply", command=self.button_pressed, font=("Helvetica", 10, "bold"))

        self.text1 = Label(self.sub, text="Full HD", font=("Helvetica", 10, "bold"))
        self.text2 = Label(self.sub, text="Full Ready", font=("Helvetica", 10, "bold"))
        self.text3 = Label(self.sub, text="Standard", font=("Helvetica", 10, "bold"))
        self.text4 = Label(self.sub, text="Frames per second", font=("Helvetica", 10, "bold"))
        self.text5 = Label(self.sub, text="Frames per second", font=("Helvetica", 10, "bold"))
        self.text6 = Label(self.sub, text="Frames per second", font=("Helvetica", 10, "bold"))

    def run(self):

        self.sub.transient(self.window)
        self.sub.title("Video Options")
        self.sub.geometry("300x250+200+100")
        self.sub.grab_set()

        self.text1.place(x=30, y=10)
        self.text4.place(x=130, y=10)
        self.radio1.place(x=30, y=30)
        self.list1.place(x=130, y=32)
        self.list1.current(0)

        self.text2.place(x=30, y=60)
        self.text5.place(x=130, y=60)
        self.radio2.place(x=30, y=80)
        self.list2.place(x=130, y=83)
        self.list2.current(0)

        self.text3.place(x=30, y=120)
        self.text6.place(x=130, y=120)
        self.radio3.place(x=30, y=140)
        self.list3.place(x=130, y=143)
        self.list3.current(0)

        self.button.place(x=130, y=200)

        self.window.wait_window(self.sub)

    def hd(self):
        if self.radioVar1.get() is 1:
            self.radio2.configure(state=DISABLED)
            self.radio3.configure(state=DISABLED)
            self.list2.configure(state=DISABLED)
            self.list3.configure(state=DISABLED)
        else:
            self.radio2.configure(state=NORMAL)
            self.radio3.configure(state=NORMAL)
            self.list2.configure(state=NORMAL)
            self.list3.configure(state=NORMAL)

    def hd_ready(self):
        if self.radioVar2.get() is 1:
            self.radio1.configure(state=DISABLED)
            self.radio3.configure(state=DISABLED)
            self.list1.configure(state=DISABLED)
            self.list3.configure(state=DISABLED)
        else:
            self.radio1.configure(state=NORMAL)
            self.radio3.configure(state=NORMAL)
            self.list1.configure(state=NORMAL)
            self.list3.configure(state=NORMAL)

    def standard(self):
        if self.radioVar3.get() is 1:
            self.radio2.configure(state=DISABLED)
            self.radio1.configure(state=DISABLED)
            self.list2.configure(state=DISABLED)
            self.list1.configure(state=DISABLED)
        else:
            self.radio2.configure(state=NORMAL)
            self.radio1.configure(state=NORMAL)
            self.list2.configure(state=NORMAL)
            self.list1.configure(state=NORMAL)

    def button_pressed(self):
        if self.radioVar1.get() is 1:
            Configuration.frames = self.list1.get()
            Configuration.quality = "1920x1080"
            self.sub.destroy()
        elif self.radioVar2.get() is 1:
            Configuration.frames = self.list2.get()
            Configuration.quality = "1280x720"
            self.sub.destroy()
        elif self.radioVar3.get() is 1:
            Configuration.frames = self.list3.get()
            Configuration.quality = "720x480"
            self.sub.destroy()
