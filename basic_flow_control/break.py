#!/usr/bin/python

#if you break loop from 'for' or 'while', the related 'else' block will not be executed

while True:
    s = raw_input('Enter something(Q to quit):')
    if s == 'q' or s=='Q' or s == 'quit':
        break
    print 'Length of the string is:',len(s)

print 'Done'
