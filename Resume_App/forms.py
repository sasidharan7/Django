from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class sec1form(forms.Form):  
    name = forms.CharField(max_length=50, required = False)
    description = forms.CharField(max_length=50, required = False)
    email = forms.CharField(max_length=100, required = False)
    stackoverflow = forms.CharField(max_length=500, required = False)
    linkedin = forms.CharField(max_length=500, required = False)
    github = forms.CharField(max_length=500, required = False)
    downloadresume = forms.CharField(max_length=500, required = False)

class sec2form(forms.Form):  
    sec2line1 = forms.CharField(max_length=50, required = False)
    sec2line2 = forms.CharField(max_length=50, required = False)
    sec2line3 = forms.CharField(max_length=100, required = False)
    sec2line4 = forms.CharField(max_length=500, required = False)
   

    