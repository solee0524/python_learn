#!/usr/bin/python
__author__ = 'oracle'

from purl import URL
from_str = URL('https://www.google.com/search?q=testing')
print from_str.query_param('q')

