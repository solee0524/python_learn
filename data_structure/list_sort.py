#!/usr/bin/python

__author__ = 'oracle'

a = [5, 2, 7, 9]
print a
a.sort(cmp)
print a

b = ['aardada', 'ds', 'ssaw', 'sisiejjas', 'ssaww']
print b
b.sort(key=len)
print b

c = [4, 6, 2, 1, 7, 9]
print c
c.sort(reverse=True)
print c

