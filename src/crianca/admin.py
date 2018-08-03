from django.contrib import admin
from .models import (Crianca, Responsavel)

admin.site.register(Responsavel)

@admin.register(Crianca)
class EscolaList(admin.ModelAdmin):
    change_list_filter_template = "admin/filter_listing.html"
    list_display = ('nome_crianca', 'responsavel','modalidade')
    list_filter = ('modalidade', 'Benedito', 'Carlos_Franca', 'Izildinha', 'Lidia_Neto', 'Nossa_Aparecida', 'Orestes', 'Sta_Clara', 'Venusta', 'Issa')
    search_fields = ('nome_crianca',)
    list_per_page = 20
    fieldsets = (
    ('Informações da Criança', {
        'fields': ('modalidade', 'nome_crianca', 'dt_nascimento', 'endereco_crianca', 'responsavel', 'status', 'observacao',)
    }),
    ('Benedito', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_benedito', 'Benedito', 'posicao_benedito')
    }),
    ('Carlos França', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_carlosF', 'Carlos_Franca', 'posicao_carlosf')
    }),
    ('Izildinha', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_izildinha', 'Izildinha', 'posicao_izildinha')
    }),
    ('Lídia', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_lidia', 'Lidia_Neto', 'posicao_lidia')
    }),
    ('Nossa Senhora Aparecida', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_aparecida', 'Nossa_Aparecida', 'posicao_aparecida')
    }),
    ('Orestes', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_orestes', 'Orestes', 'posicao_orestes')
    }),
    ('Santa Clara', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_clara', 'Sta_Clara', 'posicao_clara')
    }),
    ('Venusta', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_venusta', 'Venusta', 'posicao_venusta')
    }),
    ('Georgina', {
        'classes':('grp-collapse', 'grp-closed',),
        'fields': ('data_comparecimento_georgina', 'Issa', 'posicao_issa')
    }),
    )