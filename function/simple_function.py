#!/usr/bin/python

def sayHello():
	print 'Hello World!'

sayHello()

print '\nfunction with arguments'

def printMAX(a,b):
	if a > b:
		print a, 'is maximum'
	else:
		print b, 'is maximum'

def chechInput(a):
	if '.' in a:
		return False

printMAX(3,4);

x = raw_input('input number:')
y = raw_input('input number:')

printMAX(x,y)