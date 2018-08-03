from django.db import models


class LocalizacaoBairro(models.Model):
    bairro = models.CharField(verbose_name='bairro', max_length=60, unique=True)

    def __str__(self):
        return self.bairro

    class Meta:
        db_table = "tb_localizacao_bairro"
        verbose_name = "Localização Bairro"
        verbose_name_plural = "Localização Bairros"
        ordering = ['bairro']


class Localizacao(models.Model):
    LOCALIZACAO_CHOICE = (
        ('administracao', 'Administração e Finanças'),
        ('social', 'Assistencia Social'),
        ('educacao', 'Educação'),
        ('infra', 'Infraestrutura'),
        ('saude', 'Saúde'),
        ('esportes', 'Esportes, Cultura e Turismo'),
        ('gabinete', 'Gabinete do Prefeitu'),
        ('outros', 'Outros'),

    )
    secretaria = models.CharField(verbose_name='secretaria', max_length=30, choices=LOCALIZACAO_CHOICE)
    orgao = models.CharField(verbose_name='orgão', max_length=80)
    endereco = models.CharField(verbose_name='endereço', max_length=80)
    bairro = models.ForeignKey(LocalizacaoBairro)
    telefone = models.CharField(verbose_name='telefone(s)', max_length=80)
    horario = models.TextField(verbose_name='horario de funcionamento')

    class Meta:
        db_table = "tb_localizacao_orgaos"
        verbose_name = "Localização"
        verbose_name_plural = "Localização"
        ordering = ['orgao']

    def __str__(self):
        return self.orgao
