from django.apps import AppConfig
from pdf_process_site.settings import MEDIA_DIR
import os

class ExtractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extractor'

def handle_upload(file):
    with open(os.path.join(MEDIA_DIR, 'text.pdf'), "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    print('finished')