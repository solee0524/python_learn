#!/usr/bin/python
import requests
import json

__author__ = 'oracle'


r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']
json_string = json.loads(r.text)

print json_string

print type(json_string)

print json_string['message']

print type(json_string['message'])
