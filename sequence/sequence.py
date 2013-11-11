#!/usr/bin/env python

numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers[2:-1:2]

hello = 'Hello!'
print hello[0:4]

sentence= raw_input('Plz input a sentence: ')
text_width = len(sentence)

window_width = 80
box_width=text_width +6
left_margin = (window_width - box_width)//2
print
print ' '*left_margin + '+' + '-'*text_width + '+'
print ' '*left_margin + '|' + ' '*text_width + '|'
print ' '*left_margin + '|' + sentence + '|'
print ' '*left_margin + '|' + ' '*text_width + '|'
print ' '*left_margin + '+' + '-'*text_width + '+'
print


database = [
        ['bo','1111'],
        ['col','2222'],
        ['neo','3333']
        ]
username = raw_input('Plz input user name: ')
pin = raw_input('Pin code: ')
if [username, pin] in database: print "Access granted"

