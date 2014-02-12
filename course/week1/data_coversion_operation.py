#!/usr/bin/python

#data coversion operations
#convert an integer into string - str
#convert an hour into 24-hour format "03:00"

hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens), str(ones), ":00"
print str(tens)+str(ones)+":00"
