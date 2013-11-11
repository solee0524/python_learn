#!/usr/bin/env python

test=['to','be','or','not','to','be']
print test.count('to')

test.remove('to')
print test

test.insert(1,'to')
print test

test.pop()
print test

print test.index('to')

test.reverse()
print test

test.reverse()
test.append('be')
test.remove('to')
test.insert(0,'to')

test1 = test[:]
test1.sort()
print test
print test1
