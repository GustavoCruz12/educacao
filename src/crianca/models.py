from django.db import models


class Responsavel(models.Model):
    nome_responsavel = models.CharField(max_length=255)
    endereco_responsavel = models.CharField(max_length=255, null=True, blank=True)
    telefone_responsavel = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome_responsavel


class Crianca(models.Model):
    MODALIDADE_CHOICES = (
        ('BERCARIO 1', 'Berçário 1'),
        ('BERCARIO 2', 'Berçário 2'),
        ('MATERNAL 1', 'Maternal 1'),
        ('MATERNAL 2','Maternal 2'),
    )
    modalidade = models.CharField(max_length=20, choices=MODALIDADE_CHOICES)

    STATUS_CHOICES = (
        ('ATENDIDA', 'Atendida'),
        ('SEM CONTATO', 'Sem Contato'),
        ('AGUARDANDO VAGA', 'Aguardando Vaga'),
        ('DESISTENTE/ABANDONO', 'Desistente/Abandono'),
        ('AGUARDANDO TRANSFERENCIA', 'Aguardando Transferência'),
        ('TRANFERIDO', 'Transferido'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)

    observacao = models.CharField(max_length=500, blank=True, null=True)
    nome_crianca = models.CharField(max_length=255)
    dt_nascimento = models.CharField("Data de Nascimento", max_length=50, null=True, blank=True)
    endereco_crianca = models.CharField(max_length=255, blank=True, null=True)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)


    # data de comparecimento
    data_comparecimento_benedito = models.DateField("Data de Comparecimento Benedito", auto_now=False, blank=True, null=True)
    data_comparecimento_carlosF = models.DateField("Data de Comparecimento Carlos França", auto_now=False, blank=True, null=True)
    data_comparecimento_izildinha = models.DateField("Data de Comparecimento Izildinha", auto_now=False, blank=True, null=True)
    data_comparecimento_lidia = models.DateField("Data de Comparecimento Lídia", auto_now=False, blank=True, null=True)
    data_comparecimento_aparecida = models.DateField("Data de Comparecimento Nossa sra° Aparecida", auto_now=False, blank=True, null=True)
    data_comparecimento_orestes = models.DateField("Data de Comparecimento Orestes", auto_now=False, blank=True, null=True)
    data_comparecimento_clara = models.DateField("Data de Comparecimento Sta Clara", auto_now=False, blank=True, null=True)
    data_comparecimento_venusta = models.DateField("Data de Comparecimento Venusta", auto_now=False, blank=True, null=True)
    data_comparecimento_georgina = models.DateField("Data de Comparecimento Georgina Issa", auto_now=False, blank=True, null=True)


    # escolas
    Benedito = models.BooleanField("Vaga para Benedito?", blank=True)
    Carlos_Franca = models.BooleanField("Vaga para Carlos França?", blank=True)
    Izildinha = models.BooleanField("Vaga para Izildinha?", blank=True)
    Lidia_Neto = models.BooleanField("Vaga para Lídia Neto?", blank=True)
    Nossa_Aparecida = models.BooleanField("Vaga para Nossa sr° Aparecida?", blank=True)
    Orestes = models.BooleanField("Vaga para Orestes?", blank=True)
    Sta_Clara = models.BooleanField("Vaga para Sta Clara?", blank=True)
    Venusta = models.BooleanField("Vaga para Venusta?", blank=True)
    Issa = models.BooleanField("Vaga para Georgina Issa?", blank=True, default=False)


    #posicao por escola

    posicao_benedito = models.IntegerField("Posição do aluno no Benedito", blank=True, null=True)
    posicao_carlosf = models.IntegerField("Posição do aluno no Carlos França", blank=True, null=True)
    posicao_izildinha = models.IntegerField("Posição do aluno na Izildinha", blank=True, null=True)
    posicao_lidia = models.IntegerField("Posição do aluno na Lídia", blank=True, null=True)
    posicao_aparecida = models.IntegerField("Posição do aluno na Nossa sra° Aparecida", blank=True, null=True)
    posicao_orestes = models.IntegerField("Posição do aluno na Orestes", blank=True, null=True)
    posicao_clara = models.IntegerField("Posição do aluno na Sta Clara", blank=True, null=True)
    posicao_venusta = models.IntegerField("Posição do aluno no Venusta", blank=True, null=True)
    posicao_issa = models.IntegerField("Posição do aluno no Georgina Issa", blank=True, null=True)

    def __str__(self):
        return self.nome_crianca


