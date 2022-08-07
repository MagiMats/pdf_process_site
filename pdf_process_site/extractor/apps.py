from django.apps import AppConfig


class ExtractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'extractor'

def handle_upload(file):
    with open('C:\\Users\\matsj\\Programming\\Personal Project\\pdf_process_site\\pdf_process_site\\extractor\\file.pdf', "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    print('finished')