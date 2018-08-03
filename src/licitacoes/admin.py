#! encoding: utf-8
from django.contrib import admin
from .models import Licitacao, ArquivosLicitacao, ModalidadeLicitacao


@admin.register(ModalidadeLicitacao)
class ModalidadeLicitacaoAdmin(admin.ModelAdmin):
    pass


@admin.register(ArquivosLicitacao)
class ArquivosLicitacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'arquivo', 'publicacao',)
    search_fields = ('descricao',)
    list_per_page = 20


@admin.register(Licitacao)
class LicitacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'numero', 'ano')
    search_fields = ('descricao', 'numero', 'ano',)
    list_filter = ('ano',)
    list_per_page = 20
    filter_horizontal = ('arquivos',)
