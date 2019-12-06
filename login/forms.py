from django import forms
from django.contrib.auth.models import User
from .models import CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Your Password'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'User Name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}),
        }

class CustomUserForm (forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ('url', 'picture')
        widgets = {
            'url' : forms.URLInput(attrs={'class':'form-control', 'name':'url', 'placeholder':'Enter Your URL'}),
            'picture': forms.FileInput(),
        }
