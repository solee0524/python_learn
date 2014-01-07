#!/usr/bin/python

def func_maximum(x, y):
	if x > y:
		return x
	else:
		return y

def func_pass():
	pass

x = raw_input('input number:')
y = raw_input('input number:')
print func_maximum(x,y)

print func_pass