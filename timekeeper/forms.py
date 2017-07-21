from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import UserProfile

class TimeCardForm(forms.Form):
    project = forms.CharField(max_length=40)
    task = forms.CharField(max_length= 100)
    date = forms.DateField()
    hours = forms.IntegerField()
    expenditure = forms.IntegerField()
    expenditure_desc = forms.CharField(max_length=100)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
