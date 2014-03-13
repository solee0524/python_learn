#/usr/bin/python

__author__ = 'oracle'

from string import Template
from string import maketrans
from string import capwords

s = Template('$x, glorious $x!')
output = s.safe_substitute(x='bo')
print output

s = Template("It's ${x}tanstic")
output = s.safe_substitute(x='bo')
print output

#use dictionary
s = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'f**k'
output = s.safe_substitute(d)
print output

#join and split method
print("\n======join and split method======\n")
print "Join:"
dir = '', 'usr', 'bin', 'env'
print dir
delimiter = '/'
print delimiter.join(dir)
print "C:"+'\\'.join(dir)
print
print "Split:"
temp_str = delimiter.join(dir)
print temp_str
print temp_str.split('/')
print "Learn string in python".split()

#strip method
print("\n======strip======\n")
temp_str = "    hello, this is temp test     "
print temp_str
print temp_str.strip()
print
temp_str = "*** SPAM * for *everyone!!!  *"
print temp_str
temp_str = temp_str.strip(' *!')
print temp_str
temp_str = temp_str.split('*')
print temp_str
for n in range(len(temp_str)):
    temp_str[n] = temp_str[n].strip()
temp_str = ' '.join(temp_str)
print temp_str

#replace and translate
print("\n======replace and translate======\n")
temp_str = "this is an isolate test"
print temp_str
print temp_str.replace('is', 'H')

table = maketrans('cs', 'kz')
print table[97:123]
print temp_str.translate(table, ' ')

#other
print("\n======other======\n")
str = "This is test string"
print "Origin::", str
print ".lower()::", str.lower()
print ".title()::", str.title()
print ".capitalize()::", str.capitalize()
print ".upper()::", str.upper()
print ".swapcase()::", str.swapcase()

#capwords: split->capitalize->join
print("\n======capwords======\n")
temp_str = "oh|my|god"
print temp_str
print temp_str.capitalize()
print capwords(temp_str, '|')
