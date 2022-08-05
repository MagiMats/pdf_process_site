from django import forms
from django.core import validators

class UploadForm(forms.Form):
    name = forms.CharField(max_length=5)
    email = forms.EmailField()
    
