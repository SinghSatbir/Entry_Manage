from django import forms

from entry_app.models import Visitor, Host


class VisitorForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()



class HostForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()

class Checkout(forms.Form):
    phone=forms.CharField()