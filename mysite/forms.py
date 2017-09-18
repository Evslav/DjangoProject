from django import forms
from .models import *

class laedForm(forms.ModelForm):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)

    class Meta:
        model = lead
        exclude = [""]

class uinfo(forms.ModelForm):
    user_agent = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)

    class Meta:
        db_table = 'uinfo'
        model = uinfo
        exclude = [""]