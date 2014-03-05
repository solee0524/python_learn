#!/usr/bin/env python

test = ['to', 'be', 'or', 'not', 'to', 'be']
print test.count('to')

test.remove('to')
print test

test.insert(1, 'to')
print test

test.pop()
print test

print test.index('to')

test.reverse()
print test

test.reverse()
test.append('be')
test.remove('to')
test.insert(0, 'to')

test1 = test[:]
test1.sort()
print test
print test1


if raw_input('Plz input a character:') in 'Python':
    print("the character is in 'Python'")
else:
    print("Not in 'Python'")

"""
pay attention to copy one list to another

y = x
y.reverse()

b = a[:]
b.reverse()
"""

x = [1, 2, 3, 4, 5]
a = [1, 2, 3, 4, 5]

y = x
y.reverse()
print 'x:', x
print 'y:', y

b = a[:]
b.reverse()
print 'a:', a
print 'b:', b

