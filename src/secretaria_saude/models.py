from django.db import models
from filebrowser.fields import FileBrowseField


class SaudeEscala(models.Model):
    unidade = models.CharField('Unidade', max_length=120)
    endereco = models.CharField('Endereço', max_length=120)
    telefone = models.CharField('Telefone(s)', max_length=60)
    horario_funcionamento = models.CharField('Horário de Funcionamento', max_length=80)
    arquivo = FileBrowseField('PDF', max_length=200, directory='saude/escalas',
                              extensions=['.pdf', '.doc', 'xls', '.docx',
                              '.xlsx'], blank=True, null=True)
    dt_atualizacao = models.DateField('Data de Inclusão')

    class Meta:
        db_table = 'tb_saude_escala'
        verbose_name = 'Saúde Escala'
        verbose_name_plural = 'Saúde Escalas'
        ordering = ['unidade']

    def __str__(self):
        return self.unidade


class SaudeMedicamento(models.Model):
    TIPO_CHOICES = (
        ('faltante', 'Faltantes'),
        ('em_estoque', 'Em estoque')
    )
    status = models.CharField('STATUS', max_length=50, choices=TIPO_CHOICES, default='em_estoque')
    nome_arquivo = models.CharField('nome_arquivo', max_length=250, default="padronizado")
    arquivo = FileBrowseField('PDF', max_length=200, directory='saude/medicamentos',
                              extensions=['.pdf', '.doc', 'xls', '.docx', '.xlsx'], blank=True, null=True)
    dt_atualizacao = models.DateField('Data de Inclusão', auto_now=True)

    class Meta:
        db_table = 'tb_saude_medicamentos'
        verbose_name_plural = 'Saude medicamentos'

    def __str__(self):
        return f"{self.nome_arquivo} - ultima atualização: {self.dt_atualizacao}"