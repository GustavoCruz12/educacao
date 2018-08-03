import PyPDF2
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DiarioOficial


@receiver(post_save, sender=DiarioOficial)
def update_diario(sender, created, instance, **kwargs):
    # diario = DiarioOficial.objects.get(pk=instance.id)
    caminho = '/opt/webserver/src/'
    if created:
        pdf_file_obj = open(caminho + instance.arquivo.url, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        pdf_list = []

        for page in pdf_reader.pages:
            pdf_list.append(page.extractText())

        pdf_text = "".join(pdf_list)

        pdf_text = pdf_text.replace('\n', '')

        instance.texto_arquivo_diario = pdf_text
        instance.save()



