from django.shortcuts import render
from .forms import UploadForm

# Create your views here.
def HomeView(request):

    if request.method == "GET":
        form = UploadForm()
    else:

        form = UploadForm(request.POST)

        if form.is_valid():
            print('amoongus')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
        else:
            print('failure')
    
    return render(request, 'extractor\home.html', context={'form': form})

