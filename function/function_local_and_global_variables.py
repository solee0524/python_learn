#!/usr/bin/python


def func_local(x):
	print '\nShow local variable'
	print 'X is',x
	x = 2
	print 'Changed local x to', x



def func_global():
	print '\nShow global variable'
	global x
	print 'X is',x
	x = 2
	print 'Changed local x to', x


x = 50
func_local(x)
print 'X is still',x

func_global()
print 'X value is',x


print '\nArgument with default value'
def say(message, times=1):
	print message * times

say('Hello')
say('World',5)

print '\nFunction Key'
def func_key(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func_key(3, 7)
func_key(25, c=24)
func_key(c=50, a=100)