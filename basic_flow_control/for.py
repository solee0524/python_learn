#!/usr/bin/python
# Filename: for.py
import random

for i in "Python":
    print i

print 'The loop is over!'

print 'Another random pick test'
list_words = ['Another', 'random', 'pick', 'test']
random.shuffle(list_words)
for i in list_words:
    print i

print 'The loop is over'