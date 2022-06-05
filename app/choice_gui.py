from secret import secret
from query_framework import Database
from tkinter import *

def skipper():
    pass

class Chooser:

    def __init__(self, root):
        window = Frame(root)
        window.pack()

        self.error = Message(text = "", width = 160)
        self.label1 = Label(text = "Username")
        self.label1.pack()

        self.username = Entry(text = "")
        self.username.pack()

        self.label2 = Label(text = "Password")
        self.label2.pack()
        self.label2.config(bg='lightgreen', padx=0)

        self.password = Entry(text = "")
        self.password.pack()

        self.label3 = Label(text = "Username")
        self.label3.pack()

        self.username2 = Entry(text = "")
        self.username2.pack()

        self.label4 = Label(text = "Password")
        self.label4.pack()
        self.label4.config(bg='lightgreen', padx=0)

        self.password2 = Entry(text = "")
        self.password2.pack()

        self.label5 = Label(text = "Username")
        self.label5.pack()

        self.username3 = Entry(text = "")
        self.username3.pack()

        self.label6 = Label(text = "Password")
        self.label6.pack()
        self.label6.config(bg='lightgreen', padx=0)

        self.password3 = Entry(text = "")
        self.password3.pack()

        self.button = Button(text = "Search", command = skipper)
        self.button.pack()



def main():
    window = Tk()
    window.geometry("1200x500")
    c = Chooser(window)
    window.mainloop()


if __name__ == "__main__":
    main()
