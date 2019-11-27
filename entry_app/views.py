from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(self):
    return HttpResponse('<p>index</p>')
def hosts_form(self):
    return HttpResponse('<p>Host Forms</p>')
def hosts_names(self):
    return HttpResponse('<p>Host Names</p>')
def visitor_form(self):
    return HttpResponse('<p>Visitor Forms</p>')
def visitor_names(self):
    return HttpResponse('<p>Visitor names</p>')
def visitor_checkout(self):
    return HttpResponse('<p>Checkout Visitors Here</p>')