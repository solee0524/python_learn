#!/usr/bin/python
__author__ = 'oracle'

from Tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
top.title('scroll bar')
top.geometry('600x400')
label = Label(top, text='Hello world!', font='Helvetica -20 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=50, orient=HORIZONTAL, command=resize)
scale.set(20)
scale.pack(fill=X, expand=1)
quit = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')

quit.pack()

mainloop()