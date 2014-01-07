#!/usr/bin/python
# Filename: while.py
import random

number  = random.randint(0,20)
running = True

while running:
    guess = int(raw_input('Enter an integer :'))
    if guess == number:
        print 'Congratulations, you guessed it.' 
        running = False # this causes the while loop to stop
    elif guess > number:
        print 'You guess is higher!'
    else:
        print 'You guess is lower!'
else:
    print 'The loop is over.'


