from django.db import models
from filebrowser.fields import FileBrowseField


class Empresa(models.Model):
    CHOICES_EMPRESAS = (
        ('0', 'Manuais'),
        ('1', 'Decretos'),
        ('2', 'Instruções Normativas'),
        ('3', 'Legislação'),
        ('4', 'Formulários'),
    )
    tipo = models.CharField(u'Tipo de arquivo', max_length=60, choices=CHOICES_EMPRESAS)
    descricao = models.CharField(u'Descrição', max_length=250)
    observacao = models.CharField(u'Observação', max_length=30, blank=True)
    arquivo = FileBrowseField("Arquivo .doc ou .pdf", max_length=200, extensions=[".pdf", ".doc"],
                              directory="administracao/empresa/", blank=True, null=True)

    class Meta:
        verbose_name = "Apoio a Empresas"
        verbose_name_plural = "Apoio a Empresas"
        db_table = "tb_apoio_empresa"

    def __str__(self):
        return self.descricao


class ComunicadoEmpresa(models.Model):
    titulo = models.CharField(u'Titulo', max_length=80)
    texto = models.TextField(u'Aviso')
    data = models.DateTimeField(u'Publicacão', auto_now_add=True)

    class Meta:
        db_table = "tb_comunicado_empresa"
        verbose_name = "Comunicado para empresas"
        verbose_name_plural = "Comunicado para Empresas"

    def __str__(self):
        return self.titulo
