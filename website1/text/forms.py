from django import forms
from text.models import Log, Entry
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['username', 'email', 'password']

class LogForm(forms.ModelForm):
    #date = forms.DateTimeField(widget=forms.DateTimeField)

    class Meta:
        model = Log
        #widgets = {
        #    'datetime': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        #}
        fields = ['title', 'category']

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'text']
