#!/usr/bin/python

import Tkinter

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
top.title('my first')
top.geometry('400x200')
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
