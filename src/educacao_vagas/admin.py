from django.contrib import admin
from easy_select2 import select2_modelform

from .models import (
    Escola,
    Turma,
    Responsavel,
    Crianca,
    SolicitacaoVaga,
    Bairro,
    Logradouro,
    EnderecoCrianca,
    SolicitacaoAtendida
)

CriancaForm = select2_modelform(Crianca, attrs={'width': '650px'})
SolicitacaoVagaForm = select2_modelform(SolicitacaoVaga,
                                        attrs={'width': '450px'})
EnderecoCriancaForm = select2_modelform(EnderecoCrianca)
SolicitacaoAtendidaForm = select2_modelform(SolicitacaoAtendida)
TurmaForm = select2_modelform(Turma)


@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    pass


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('desc_turma', 'ano', 'escola')
    ordering = ('escola', 'desc_turma')


# @admin.register(Responsavel)
# class ResponsavelAdmin(admin.ModelAdmin):
#     list_display = ('nome_responsavel', 'telefone')

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    ordering = ('bairro',)


@admin.register(Logradouro)
class LogradouroAdmin(admin.ModelAdmin):
    ordering = ('endereco',)


class EnderecoCriancaInline(admin.TabularInline):
    form = EnderecoCriancaForm
    model = EnderecoCrianca
    extra = 0
    max_num = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class SolicitacaoAtendidaInline(admin.StackedInline):
    form = SolicitacaoAtendidaForm
    model = SolicitacaoAtendida
    extra = 0
    max_num = 1
    classes = ('grp-collapse grp-open',)
    # inline_classes = ('grp-collapse grp-open',)


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    ordering = ('nome_responsavel',)


@admin.register(Crianca)
class CriancaAdmin(admin.ModelAdmin):
    form = CriancaForm
    list_display = ('nome_crianca', 'responsavel', 'endereco',)

    inlines = [
        EnderecoCriancaInline
    ]


@admin.register(SolicitacaoVaga)
class SolicitacaoVagaAdmin(admin.ModelAdmin):
    list_editable = ('status',)
    # radio_fields = {"status": admin.HORIZONTAL}
    form = SolicitacaoVagaForm
    read_only = ['atendida_flag']
    list_display = ('crianca', 'dt_solicitacao', 'turmas_preferencia', 'observacao', 'status')
    list_filter = ('turma_preferencia', 'status')
    search_fields = ('crianca__nome_crianca',)

    inlines = [
        SolicitacaoAtendidaInline
    ]
