from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from django.template import loader

from entry_app.forms import HostForm,VisitorForm
from entry_app.models import Visitor,Host

def index(request):
    template = loader.get_template('index.html')
    context = {
        'visitor_all' : Visitor.objects.all(),
        'Host_all' : Host.objects.all(),
    }
    return HttpResponse(template.render(context, request))
def hosts_form(request):
    template = loader.get_template('hform.html')
    form_object = HostForm()
    if request.method == 'POST':
        form_object = HostForm(request.POST)
        if form_object.is_valid():
            form_object.save(commit=True)
            return index(request)
    context = {
        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))

def visitor_form(request):
    template = loader.get_template('vform.html')
    form_object = VisitorForm()
    if request.method == 'POST':
        form_object = VisitorForm(request.POST)
        if form_object.is_valid():
            form_object.save(commit=True)
            return index(request)
    context = {
        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))

def visitor_checkout(self):
    return HttpResponse('<p>Checkout Visitors Here</p>')