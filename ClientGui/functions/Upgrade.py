from tkinter import Tk, messagebox

class Upgrade:

    def __init__(self):
        root = Tk()
        root.withdraw()
        messagebox.askokcancel("Upgrade", "There is a new Upgrade for this Gui Available to download on GamingServer Website")
