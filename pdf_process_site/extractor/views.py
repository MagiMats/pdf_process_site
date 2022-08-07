from django.shortcuts import render
from .forms import UploadForm
from .apps import handle_upload
from django.http import HttpResponseRedirect

# Create your views here.
def HomeView(request):

    if request.method == "GET":
        form = UploadForm()
    else:

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            upload = form.cleaned_data["upload"]
            handle_upload(request.FILES["upload"])

            return HttpResponseRedirect('/succes/')
            
    return render(request, 'extractor\home.html', context={'form': form})

def SuccesView(request):
    return render(request, 'extractor\succes.html')
