#!/usr/bin/python

__author__ = 'oracle'

import string

width = input('please input width:')

if width < 30:
    width = 30

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
body_format = '%-*s%*.2f'

print '=' * width

print header_format % (item_width, 'Item', price_width, 'Price($)')

print '-' * width

print body_format % (item_width, 'Apples', price_width, 0.9)
print body_format % (item_width, 'Pears', price_width, 0.50)
print body_format % (item_width, 'Cantaloupes', price_width, 1.92)
print body_format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8)
print body_format % (item_width, 'Prunes (4 lbs)', price_width, 12)
print body_format % (item_width, 'Bananas', price_width, 7)
print body_format % (item_width, 'Milk (1 bottle)', price_width, 2)

print '=' * width

output = 'Hello, this is test string module'
print(output)
print(output.upper())
print(output[0].isupper())

print(output.count('s'))

print(output.find('this'))
print(output.find('this', 8))
print(output.find('this', 1, 7))
