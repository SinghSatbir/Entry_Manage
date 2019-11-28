

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader
from entry_app.forms import HostForm, VisitorForm, Checkout
from entry_app.models import Visitor,Host


def index(request):
    template = loader.get_template('index.html')
    context = {
        'v_all' : Visitor.objects.all(),
        'a_host' : Host.objects.last(),
    }
    return HttpResponse(template.render(context, request))
def hosts_form(request):
    template = loader.get_template('hform.html')
    form_object = HostForm()
    if request.method == 'POST':
        form_object = HostForm(request.POST)
        if form_object.is_valid():
            entered_name = form_object.cleaned_data['name']
            entered_email = form_object.cleaned_data['email']
            entered_phone = form_object.cleaned_data['phone']
            Host.objects.get_or_create(name=entered_name, email=entered_email, phone=entered_phone)
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
            entered_name = form_object.cleaned_data['name']
            entered_email = form_object.cleaned_data['email']
            entered_phone = form_object.cleaned_data['phone']
            current_host=Host.objects.last()
            Visitor.objects.get_or_create(name=entered_name, email=entered_email, phone=entered_phone,hostname=current_host.name)
            last_val=Visitor.objects.last()
            message='\nName : '+str(entered_name)+'\n Email : '+str(entered_email)+'\n Phone : '+str(entered_phone)+'\n Checkin : '+str(last_val.check_in)
            send_mail(subject="Visitor Entry Details",from_email=settings.EMAIL_HOST_USER,message=message,recipient_list=[current_host.email,'entry.manage.satbir@gmail.com'],auth_password=settings.EMAIL_HOST_PASSWORD)
            return index(request)
    context = {
        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))

def visitor_checkout(request):
    template = loader.get_template('vform.html')
    form_object = Checkout()
    if request.method == 'POST':
        form_object = Checkout(request.POST)
        if form_object.is_valid():
            entered_phone = form_object.cleaned_data['phone']
            Visitor.objects.filter(phone=entered_phone).update(phone=entered_phone)
            visitor_co = Visitor.objects.get(phone=entered_phone)
            message='\nName : '+str(visitor_co.name)+'\n Email : '+str(visitor_co.email)+'\n Phone : '+str(entered_phone)+'\n Checkin : '+str(visitor_co.check_in)+'\n Checkout : '+str(visitor_co.check_out)+'\n Host : '+str(visitor_co.hostname)
            send_mail(subject="Visitor Entry Details", from_email=settings.EMAIL_HOST_USER, message=message,
                      recipient_list=[visitor_co.email, 'entry.manage.satbir@gmail.com'],
                      auth_password=settings.EMAIL_HOST_PASSWORD)
            return index(request)
    context = {
        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))