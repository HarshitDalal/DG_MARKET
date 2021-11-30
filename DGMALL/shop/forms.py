from django import forms
from django.db import models
from django.forms import fields, widgets
from shop.models import ContactUs, UserDetails
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Create forms here
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name','email','mobile','decp')
        labels = {'name':'Full Name','email':'Email','mobile':'Mobile no','decp':'Descpriction'}
        
class RegistrationForm(UserCreationForm):
    password2 = forms.CharField(required=True,label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email']
        labels = {'email': 'Email','username':'Username'}

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        exclude = ['user']

class AdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}
       