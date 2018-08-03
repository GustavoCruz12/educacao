from django.contrib import admin
from localizacao_orgaos.models import Localizacao, LocalizacaoBairro


@admin.register(LocalizacaoBairro)
class LocalizacaoBairroAdmin(admin.ModelAdmin):
    pass


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('orgao', 'secretaria', 'endereco',)
    list_filter = ('secretaria',)
    search_fields = ('orgao', 'endereco',)