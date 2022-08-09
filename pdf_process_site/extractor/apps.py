from django.apps import AppConfig
from pdf_process_site.settings import MEDIA_DIR
import os, fitz

class ExtractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extractor'

