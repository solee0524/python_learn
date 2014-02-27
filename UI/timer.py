#!/usr/bin/python

#use timer with Canvas change text
__author__ = 'oracle'
from Tkinter import *
from time import sleep
from threading import Timer


counter = 0
timer1 = None
t_message = None


def increase():
    global counter
    global timer1
    counter += 1
    print counter
    timer1 = Timer(1, increase)
    timer1.start()


def quit_window():
    global timer1
    timer1.cancel()
    top.quit()


def change_canvas():
    global t_message
    global counter
    canvas1.itemconfigure(t_message, state="hidden")
    t_message = canvas1.create_text(150, 100, text=counter, fill='red', font=helv30)


top = Tk()
top.title('timer test')
top.geometry('500x300')

helv30 = ('Helvetica', 30)  #font

frame1 = Frame(top)
frame1.grid(row=0, column=0)

canvas1 = Canvas(top, width=300, height=200, bg='black')
canvas1.grid(row=0, column=1)

t_message = canvas1.create_text(150, 100, text=counter, fill='red', font=helv30)

start_button = Button(frame1, text="start", width=20, command=increase)
start_button.grid(row=0, column=0, padx=15, pady=2)
show_button = Button(frame1, text="show", width=20, command=change_canvas)
show_button.grid(row=2, column=0, padx=15, pady=2)
quit_button = Button(frame1, text="quit", width=20, command=quit_window)
quit_button.grid(row=4, column=0, padx=15, pady=2)

mainloop()