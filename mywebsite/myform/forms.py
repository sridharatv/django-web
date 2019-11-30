from django import forms
from django.core import validators
from profanity_check import predict, predict_prob
from myform.models import User

class NewUserForm (forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'