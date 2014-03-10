#! /usr/bin/python

__author__ = 'oracle'

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World, python web!")