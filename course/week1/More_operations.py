#!/usr/bin/python

import math
import random

# get digits of number
num = 35
tens = num // 10
ones = num % 10

print tens, ones
print 10 * tens + ones

#24 hour clock - application
hour = 20
shift = 8
print (hour + shift) % 24


#application - screen wraparound
# Spaceship form week seven

width = 800

position = 797
move = 5
position = (position + move) % width
print position

move1 = -5
position1 = 2
position1 = (position1 + move1) % width
print position1



print math.pi


