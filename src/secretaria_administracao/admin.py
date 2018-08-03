from django.contrib import admin
from .models import Empresa, ComunicadoEmpresa


@admin.register(Empresa)
class ApoioEmpresaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao', 'arquivo',)
    list_filter = ('tipo',)
    search_fields = ('descricao',)
    list_per_page = 20


@admin.register(ComunicadoEmpresa)
class ComunicadoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    date_hierarchy = 'data'

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]
