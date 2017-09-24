from django.contrib.auth.models import User
from django import forms
from .models import customers


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['Phone', 'Name', 'Email']