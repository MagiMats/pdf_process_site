from django.apps import AppConfig
from pdf_process_site.settings import MEDIA_DIR
import os, fitz

class ExtractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extractor'

def handle_upload(file):
    with open(os.path.join(MEDIA_DIR, "test.pdf"), "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
    doc = fitz.open("media/test.pdf")
    filename = "media/" + doc.metadata["title"] + ".pdf"
    doc.close()
    os.rename('media/test.pdf', filename)

    print('finished')