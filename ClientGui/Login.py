from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from PIL import Image, ImageDraw, ImageTk, ImageFont

from ClientGui.DatbaseCheck import DatabaseCheck
from ClientGui.MainGui import MainGui


class Login:

    def __init__(self, sock):
        self.window = Tk()
        self.socket = sock
        self.window.title("Login")
        # root.wm_attributes('-alpha', 0.5)
        self.image_file = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\WebpNetResizeimage.jpg"
        self.small_image = r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\5.jpg"
        self.window.resizable(width=False, height=False)
        self.window.geometry("%sx%s" % (1000, 500))
        self.username = StringVar()
        self.password = StringVar()

    def run(self):

        image = Image.open(self.image_file)
        images = Image.open(self.small_image)

        draw = ImageDraw.Draw(image)

        text_x = 250
        text_y = 200
        title = "Gaming Server Login"
        user = "User Name"
        password = "Password"

        font = ImageFont.truetype(r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\PaladinFLF.ttf", 30)
        title_font = ImageFont.truetype(r"C:\Users\neilm\PycharmProjects\GamingGui\ClientGui\Pictures\PaladinFLF.ttf", 50)
        draw.text((text_x + 10, text_y - 150), title, fill="yellow", font=title_font)
        draw.text((text_x - 50, text_y - 4), user, fill="yellow", font=font)
        draw.text((text_x - 50, text_y + 96), password, fill="yellow", font=font)

        photoimage = ImageTk.PhotoImage(image)
        photo = ImageTk.PhotoImage(images)
        Label(self.window, image=photoimage).place(x=0, y=0)
        Label(self.window, image=photo, bg='black').place(x=150, y=30)
        Label(self.window, image=photo, bg='black').place(x=800, y=30)

        Entry(self.window, background="white", textvariable=self.username)\
            .place(x=text_x + 110, y=text_y, width=350, height=25)
        Entry(self.window, background="white", show='*', textvariable=self.password)\
            .place(x=text_x + 110, y=text_y + 100, width=350, height=25)
        Button(self.window, text="Login", background="purple", command=self.buttonPressed)\
            .place(x=text_x + 230, y=text_y + 200, width=100, height=25)

        self.window.mainloop()

    def buttonPressed(self):
        if self.username.get() is not None and self.password.get() is not None:
            if DatabaseCheck(self.username.get(), self.password.get(), None, self.socket).check_user() is True:
                MainGui(self.window, self.socket).run()
            else:
                messagebox.showerror("Incorrect Details", "The Details are incorrect")
                self.username.set("")
                self.password.set("")
