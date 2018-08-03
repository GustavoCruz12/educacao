from django.db import models
from django.utils import timezone
from filebrowser.fields import FileBrowseField


class TipoConcurso(models.Model):
    descricao = models.CharField(verbose_name='descrição', max_length=80)

    class Meta:
        db_table = "tb_tipo_concurso"
        verbose_name = "Tipo"
        verbose_name_plural = "Tipo"

    def __str__(self):
        return self.descricao


class ArquivosConcurso(models.Model):
    descricao = models.CharField(verbose_name='descrição', max_length=200)
    arquivo = FileBrowseField("PDF", max_length=200, directory="concursos/",
                              extensions=[".pdf", ".doc", "xls", ".docx", ".xlsx"],
                              blank=True, null=True)
    publicacao = models.DateTimeField(verbose_name='data da publicação',
                                      blank=True,
                                      default=timezone.now)

    class Meta:
        db_table = "tb_arquivos_concurso"
        verbose_name = "Arquivos Concrusos"
        verbose_name_plural = "Arquivos concursos"
        ordering = ['-publicacao']




    def __str__(self):
        return self.descricao


class Concurso(models.Model):
    tipo = models.ForeignKey(TipoConcurso)
    descricao = models.CharField(verbose_name='descrição', max_length=300)
    numero = models.IntegerField(verbose_name='numero')
    ano = models.IntegerField(verbose_name='ano')
    arquivos = models.ManyToManyField(ArquivosConcurso)
    observacoes = models.TextField(blank=True)

    class Meta:
        db_table = "tb_concurso"
        verbose_name = "Concurso"
        verbose_name_plural = "Concursos"

    def __str__(self):
        return self.descricao
