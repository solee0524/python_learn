#!/usr/bin/python

__author__ = 'solee'

from random import *
from Tkinter import *

random_number = 0
range_min_number = 0
range_max_number = 0
guess_min_number = 0
guess_max_number = 0
helv11 = ('Helvetica', 11)
helv16 = ('Helvetica', 16)


def new_game():
    pass


def range100():
    global random_number
    global range_min_number
    global range_max_number
    global guess_min_number
    global guess_max_number
    global v
    range_min_number = 1
    range_max_number = 100
    guess_min_number = range_min_number
    guess_max_number = range_max_number
    random_number = randint(range_min_number, range_max_number)
    v.set("range 1 to 100")
    input_box.delete(0, END)


def range1000():
    global random_number
    global range_min_number
    global range_max_number
    global guess_min_number
    global guess_max_number
    global v
    range_min_number = 1
    range_max_number = 1000
    guess_min_number = range_min_number
    guess_max_number = range_max_number
    random_number = randint(range_min_number, range_max_number)
    v.set("range 1 to 1000")
    input_box.delete(0, END)


def input_guess(guess_number):
    global random_number
    global range_min_number
    global range_max_number
    global guess_min_number
    global guess_max_number
    global v
    guess_number = float(guess_number)
    random_number = float(random_number)
    range_min_number = float(range_min_number)
    range_max_number = float(range_max_number)
    print guess_number, range_min_number, range_max_number, random_number

    if guess_min_number == guess_max_number:
        v.set("Please select range to start")
        return None

    if (guess_number < range_min_number) or (guess_number > range_max_number):
        v.set("input is out of range")
        return None

    if guess_number < random_number:
        if guess_number > guess_min_number:
            guess_min_number = guess_number
        v.set("lower ( " + str(int(guess_min_number)) + " to " + str(int(guess_max_number)) + " )")
    elif guess_number > random_number:
        if guess_number < guess_max_number:
            guess_max_number = guess_number
        v.set("higher ( " + str(int(guess_min_number)) + " to " + str(int(guess_max_number)) + " )")
    else:
        guess_min_number = guess_number
        guess_max_number = guess_number
        v.set("correct")


def enter_guess(event):
    global v
    v.set("")
    guess_number = input_box.get()
    input_guess(guess_number)


win = Tk()
win.title('guess number')
win.geometry('700x300')

#frame1 contain two range button and one input box
#frame2 contain output label
frame1 = Frame(win)
frame1.grid(row=0, column=0)

frame2 = Frame(win)
frame2.grid(row=0, column=1)

button_range100 = Button(frame1, text='range 1 to 100', width=30, command=range100)
button_range100.grid(row=0, column=0, padx=10, pady=3)

button_range1000 = Button(frame1, text='range 1 to 1000', width=30, command=range1000)
button_range1000.grid(row=2, column=0, padx=10, pady=3)

label1 = Label(frame1, text='Enter guess number:', font=helv11)
label1.grid(row=4, column=0)

v = StringVar()
label_output = Label(frame2, textvariable=v, font=helv16, width=30)
label_output.grid(row=0, column=0)
v.set("hello")

input_box = Entry(frame1)
input_box.grid(row=5, column=0)
input_box.bind('<Return>', enter_guess)

mainloop()

