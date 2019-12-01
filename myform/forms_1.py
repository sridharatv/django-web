from django import forms
from django.core import validators
#from profanity_check import predict, predict_prob

def text_validator(value):
    pass
"""
    if predict([value]):
        raise forms.ValidationError("Got a bad word")
    if predict_prob([value]) > 0.4:
        raise forms.ValidationError("Got a probable bad word")
"""


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Email again")
    text = forms.CharField(widget=forms.Textarea,
                           validators=[text_validator])

    # Put in some security
    botcatch = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])

    # Clean the entire object and valiate specific param
    def clean(self):
        clnd_data = super().clean()
        email = clnd_data['email']
        vemail = clnd_data['verify_email']
        if email != vemail:
            raise forms.ValidationError("Both Emails does not match")
"""
    def clean_botcatch(self):
        btc = self.cleaned_data['botcatch']
        if btc:
            raise forms.ValidationError("Bot is Filling Form")
        return btc
"""

