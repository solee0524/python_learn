#!/usr/bin/python

from Tkinter import *
import tkMessageBox


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.quit = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.quit.pack(side=LEFT)
        self.hi = Button(frame, text="Hello", command=self.say_hi)
        self.hi.pack(side=LEFT)

    def say_hi(self):
        print "Hi, this is a class example."
        tkm = tkMessageBox
        tkm.showinfo("Say Hello", "Hi, this is a class example.")

win = Tk()
win.title("two button example")
win.geometry("400x200")
app = App(win)
win.mainloop()