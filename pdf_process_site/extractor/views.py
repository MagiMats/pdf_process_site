from django.shortcuts import render
from .forms import UploadForm
from .scripts import handle_upload
from django.http import HttpResponseRedirect
from notion.client import NotionClient

notion_token = "324adbe39d1b03a9898527670c93546856531f91feb5b841898cf4d9616d2ec26b0c1bc59b5f3bf3be658ca42965c4c326875092110fda731eaaac7d1a021630f7a8677a659965a40188a15ce015"
# Create your views here.
notion_client = NotionClient(token_v2=notion_token) 
def HomeView(request):

    if request.method == "GET":
        form = UploadForm()
    else:

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            upload = form.cleaned_data["upload"]
            database_url = form.cleaned_data["database_url"]
            link_url = form.cleaned_data["link_url"]

            database = notion_client.get_block(database_url)
            row = database.collection.add_row()

            row.Daily_Tracking = link_url
            handle_upload(request.FILES["upload"])


            return HttpResponseRedirect('/succes/')
            
    return render(request, 'extractor\home.html', context={'form': form})

def SuccesView(request):
    return render(request, 'extractor\succes.html')
