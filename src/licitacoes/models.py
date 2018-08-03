from django.db import models
from filebrowser.fields import FileBrowseField


class ModalidadeLicitacao(models.Model):
    descricao = models.CharField(verbose_name='descrição', max_length=80)

    class Meta:
        db_table = "tb_modalidade_licitacao"
        verbose_name = "Modalidade Licitação"
        verbose_name_plural = "Modalidades licitação"

    def __str__(self):
        return self.descricao


class ArquivosLicitacao(models.Model):
    descricao = models.CharField(verbose_name='descrição', max_length=200)
    arquivo = FileBrowseField("PDF", max_length=200, directory="licitacao/", extensions=[".pdf", ".doc", ".xls", ".docx", ".xlsx", ".dwg", ".bak", ".DWG", ".BAK", ".jpg", ".JPG", ".jpeg", ".bmp", ".plt", ".PLT"], blank=True, null=True)
    publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True, blank=True)

    class Meta:
        db_table = "tb_arquivos_licitacao"
        verbose_name = "Arquivos licitacao"
        verbose_name_plural = "Arquivos Licitação"

    def __str__(self):
        return self.descricao


class Licitacao(models.Model):
    modalidade = models.ForeignKey(ModalidadeLicitacao)
    descricao = models.CharField(verbose_name='descrição', max_length=300)
    numero = models.IntegerField(verbose_name='numero')
    ano = models.IntegerField(verbose_name='ano')
    arquivos = models.ManyToManyField(ArquivosLicitacao)

    class Meta:
        db_table = "tb_licitacao"
        verbose_name = "Licitação"
        verbose_name_plural = "Licitações"

    def __str__(self):
        return self.descricao
