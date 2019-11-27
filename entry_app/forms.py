from django import forms

from entry_app.models import Visitor, Host


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = '__all__'