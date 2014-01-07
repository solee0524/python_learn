#!/usr/bin/python
# Filename: for.py
import random

for i in "Python":
    print i
print 'The loop is over!\n'

print 'Another random pick test\n'
list_words = ['Another', 'random', 'pick', 'test']
print "The original sequence is:",
for i in list_words:
    print i,
print
random.shuffle(list_words)
print 'After shuttle:',
for i in list_words:
    print i,
print '\nThe loop is over!\n'
