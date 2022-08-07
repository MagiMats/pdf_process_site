from django import forms
from django.core import validators

class UploadForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'text'}) )
    database_url = forms.URLField()
    upload = forms.FileField()
    
