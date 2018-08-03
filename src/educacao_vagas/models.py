from django.db import models


class Escola(models.Model):
    nome_escola = models.CharField('Escola', max_length=100)

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
        db_table = 'educacao_vagas_escola'

    def __str__(self):
        return f"{self.nome_escola}"


class Turma(models.Model):
    desc_turma = models.CharField('turma', max_length=80)
    ano = models.IntegerField('Ano',)
    escola = models.ForeignKey(Escola, related_name='escolas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Turma/Escola'
        verbose_name_plural = 'Turmas/Escolas'
        db_table = 'educacao_vagas_turma_escola'

    def __str__(self):
        return f"{self.escola.nome_escola} - {self.desc_turma}"


class Bairro(models.Model):
    bairro = models.CharField('bairro', max_length=60, unique=True)

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
        db_table = 'educacao_vagas_bairro_responsavel'

    def __str__(self):
        return self.bairro


class Logradouro(models.Model):
    endereco = models.CharField('Logradouro', max_length=80, unique=True)

    class Meta:
        verbose_name = 'Logradouro'
        verbose_name_plural = 'Logradouros'
        db_table = 'educacao_vagas_endereco'

    def __str__(self):
        return self.endereco


class Responsavel(models.Model):
    nome_responsavel = models.CharField('Responsável', max_length=80)
    rg_responsavel = models.CharField('RG', max_length=14)
    telefone = models.CharField('Telefone(s)', max_length=60)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'
        db_table = 'educacao_vagas_responsavel'

    def __str__(self):
        return f"{self.nome_responsavel} - RG: {self.rg_responsavel}"


class Crianca(models.Model):
    nome_crianca = models.CharField('Nome da criança', max_length=80)
    responsavel = models.ForeignKey(Responsavel, related_name='responsaveis', on_delete=models.CASCADE)
    dt_nascimento = models.DateField('Data de nascimento')

    class Meta:
        verbose_name = 'Criança'
        verbose_name_plural = 'Crianças'
        db_table = 'educacao_vagas_crianca'

    def __str__(self):
        # resp = ", ".join([str(r) for r in self.responsaveis.all()])
        # return f"{self.nome_crianca} - Resp: {resp}"
        return self.nome_crianca

    def endereco(self):
        end = (EnderecoCrianca.objects.get(id=self.id))
        return end

    def status(self):
        sts = SolicitacaoVaga.objects.values_list('status', flat=True).get(crianca_id=self.id)
        return sts


class EnderecoCrianca(models.Model):
    crianca = models.ForeignKey(Crianca, related_name='criancas_enderecos', on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, related_name='bairros_criancas', on_delete=models.CASCADE)
    logradouro = models.ForeignKey(Logradouro, related_name='logradouros_criancas', on_delete=None)
    complemento = models.CharField('complemento', max_length=80, null=True, blank=True)
    numero = models.CharField('número', max_length=30)

    class Meta:
        verbose_name = 'Logradouro criança'
        db_table = 'educacao_endereco_crianca'

    def __str__(self):
        return f"Endereço: {self.logradouro.endereco}, {self.numero} - {self.bairro.bairro}"


# class StatusSolicitacao(models.Model):
#     status = models.CharField('status', max_length=30)
#     descricao = models.CharField('descrição', max_length=80)

#     class Meta:
#         verbose_name = 'Status solicitação'
#         verbose_name_plural = 'Status solicitações'
#         db_table = 'status_solicitacao'

#     def __str__(self):
#         return self.status


class SolicitacaoVaga(models.Model):
    AGUARDANDO_VAGA = 1
    NAO_COMPARECEU = 2
    AGUARDANDO_VAGA_TRANSFERENCIA = 3
    ATENDIDO = 4

    STATUS_CHOICES = (
        (AGUARDANDO_VAGA, 'Aguardando vaga'),
        (NAO_COMPARECEU, 'Sem contato/Não compareceu após contato'),
        (AGUARDANDO_VAGA_TRANSFERENCIA, 'Aguardando vaga para transferência'),
        (ATENDIDO, 'Atendido'),
    )

    SIM = True
    NAO = False
    ATENDIDA_CHOICE = (
        (True, 'sim'),
        (False, 'não'),

    )
    crianca = models.ForeignKey(Crianca, related_name='criancas', on_delete=models.CASCADE)
    turma_preferencia = models.ManyToManyField(Turma, related_name='turmas')
    status = models.PositiveSmallIntegerField('status', choices=STATUS_CHOICES)
    dt_solicitacao = models.DateTimeField('Data da solicitação')
    observacao = models.TextField('Observação', max_length=4000)
    dt_alteracao = models.DateTimeField('data alteração', auto_now=True)
    atendida_flag = models.BooleanField('atendida flag', default=False)

    class Meta:
        verbose_name = 'Solicitação vaga'
        verbose_name_plural = 'Solicitações vagas'
        db_table = 'educacao_vagas_solicitacao'

    def __str__(self):
        return self.crianca.nome_crianca

    def turmas_preferencia(self):
        # return "\n".join([str(p) for p in self.turma_preferencia.all()])
        return ', '.join([str(tp) for tp in self.turma_preferencia.all()])

    turmas_preferencia.short_description = 'Turmas de preferência'
    turmas_preferencia.allow_tags = True


class SolicitacaoAtendida(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoVaga, related_name="solicitacoes",
                                    on_delete=models.CASCADE, editable=False)
    dt_atendimento = models.DateTimeField('data de atendimento', auto_now=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    observacao = models.TextField('observação')

    class Meta:
        verbose_name = 'Solicitação atendida'
        verbose_name_plural = 'Atendimento solicitação'
        db_table = 'educacao_atendimento_solicitacao_vagas'

    def __str__(self):
        return f"{self.solicitacao.crianca.nome_crianca} - {self.turma.escola} {self.turma}"

