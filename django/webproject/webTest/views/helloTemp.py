#!/usr/bin/python

__author__ = 'oracle'

from django.http import HttpResponse

def index(request):
    file_handler = open('views/index.html')
    output = file_handler.read()
    # template = loader.get_template(root_path+'/index.html')
    return HttpResponse(output)
