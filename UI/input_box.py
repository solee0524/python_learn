#!/usr/bin/python

__author__ = 'oracle'

from Tkinter import *

win = Tk()
win.title('input box example')
win.geometry('500x300')

frame = Frame(win)
frame.pack()

input_text_box = Entry(frame, width=40)
input_text_box.grid(row=2, column=0)
input_text_box.delete(0, END)
input_text_box.insert(0, 'Input text here')


def call_input():
    temp_str = input_text_box.get()
    if (temp_str != '') and temp_str is not None:
        print temp_str


def call_input_enter(event):
    temp_str = input_text_box.get()
    if (temp_str != '') and temp_str is not None:
        print temp_str


def set_focus_on_textbox(event):
    # print event.x, event.y
    input_text_box.delete(0, END)
    input_text_box.focus_set()


output_button = Button(frame, text='Print', command=call_input)
output_button.grid(row=4, column=0)

input_text_box.bind('<Button-1>', set_focus_on_textbox)
input_text_box.bind('<Return>', call_input_enter)

mainloop()
