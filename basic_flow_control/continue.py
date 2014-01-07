#!/usr/bin/python

i = 3

print 'If length of input string is less than',i, ', the loop will continue.'

while True:
    s = raw_input('Enter:')
    if len(s) < i:
        continue
    print 'length is larger than',i
    break

print 'Done'

