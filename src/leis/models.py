from django.db import models
from filebrowser.fields import FileBrowseField


class Lei(models.Model):

    CHOICE_TIPO_LEI = (
        ('complementar', 'Lei complementar'),
        ('ordinaria', 'Lei ordinária'),
        ('decreto', 'Decreto'),
        ('portaria', 'Portaria'),
        ('convenio', 'Convênios Municipais'),
    )

    numero = models.IntegerField()
    tipo_lei = models.CharField(u'Tipo do documento', max_length=15, choices=CHOICE_TIPO_LEI)
    ano = models.CharField(max_length=4)
    titulo = models.TextField()
    arquivo = FileBrowseField("Arquivo PDF", max_length=200, extensions=[".pdf",".doc", ".xls", ".docx", ".xlsx"], directory="leis/", blank=True, null=True)
    publicacao = models.DateTimeField(u'publicação', auto_now=True, blank=True)

    class Meta:
        db_table = "tb_lei"
        verbose_name = "Lei"
        verbose_name_plural = "Leis"

    def __str__(self):
        return self.titulo