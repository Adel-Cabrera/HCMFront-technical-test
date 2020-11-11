from django import forms
# from django.forms import ModelForm

from .models import *


class WorkhourForm(forms.ModelForm):
    class Meta:
        model = Workhours
        # fields = ['name',
        #           'code']
        fields = "__all__"
