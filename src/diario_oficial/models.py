from django.db import models
from filebrowser.fields import FileBrowseField


class DiarioOficial(models.Model):

    CHOICE_MES = (
        ('janeiro', 'janeiro'),
        ('fevereiro', 'fevereiro'),
        ('marco', 'março'),
        ('abril', 'abril'),
        ('maio', 'maio'),
        ('junho', 'junho'),
        ('julho', 'julho'),
        ('agosto', 'agosto'),
        ('setembro', 'setembro'),
        ('outubro', 'outubro'),
        ('novembro', 'novembro'),
        ('dezembro', 'dezembro'),
    )
    CHOICES_TIPO = (
        (1, 'EDIÇÃO REGULAR'),
        (2, 'EDIÇÃO EXTRA'),
    )
    tipo = models.PositiveIntegerField('Tipo de Diario', choices=CHOICES_TIPO, default=1)
    numero = models.IntegerField('numero')
    ano = models.IntegerField('ano')
    mes = models.CharField('mês', max_length=15, choices=CHOICE_MES)
    arquivo = FileBrowseField("Arquivo", max_length=200, extensions=[".pdf",".doc", ".xls", ".docx", ".xlsx"], directory="diario_oficial/", blank=True, null=True)
    publicacao = models.DateField('publicação')

    texto_arquivo_diario = models.TextField('texto do arquivo convertido', blank=True, null=True)

    class Meta:
        db_table = "tb_diario_oficial"
        verbose_name = "Diário Oficial"
        verbose_name_plural = "Diário Oficial"

    def __str__(self):
        return f"{self.numero} - {self.mes}/{self.ano}"


class DiarioOficialExtraArquivos(models.Model):
    diario = models.ForeignKey(DiarioOficial, related_name='diarios')
    descricao = models.CharField(verbose_name='descrição', max_length=200)
    arquivo = FileBrowseField("PDF", max_length=200, directory="diario_oficial/", extensions=[".pdf", ".doc", ".xls", ".docx", ".xlsx", ".dwg", ".bak", ".DWG", ".BAK", ".jpg", ".JPG", ".jpeg", ".bmp", ".plt", ".PLT"], blank=True, null=True)
    publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True, blank=True)

    class Meta:
        db_table = "tb_diario_extra_arquivos"
        verbose_name = "Diario Oficial Arquivo Extra"
        verbose_name_plural = "Diario Oficial Arquivos Extras"

    def __str__(self):
        return self.descricao