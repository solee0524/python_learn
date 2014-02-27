#!/usr/bin/python
__author__ = 'bo li'

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


def hello():
    print('hello')


def about():
    w = Label(win, text="I am developer. See my website: solee.me")
    w.pack(side=TOP)


win = Tk()
win.title("menu example")
win.geometry("400x200")
app = App(win)

menubar = Menu(win)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

win.config(menu=menubar)
win.mainloop()
