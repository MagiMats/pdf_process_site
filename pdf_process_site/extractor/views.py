from django.shortcuts import render
from .forms import UploadForm

# Create your views here.
def HomeView(request):
    if request.method == "POST":
        form = UploadForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print('name: '+ str(name))
            print('email: ' + str(email))

    return render(request, 'extractor\home.html', {'test':UploadForm})
