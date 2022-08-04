from django import forms

class UploadForm(forms.Form):
    title = "Upload your stuff here please!"
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
