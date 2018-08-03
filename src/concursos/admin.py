
from django.contrib import admin
from concursos.models import TipoConcurso, ArquivosConcurso, Concurso


@admin.register(TipoConcurso)
class TipoConcursoAdmin(admin.ModelAdmin):
    pass


@admin.register(ArquivosConcurso)
class ArquivosConcursoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'arquivo', 'publicacao',)
    search_fields = ('descricao',)
    list_per_page = 20


@admin.register(Concurso)
class ConcursoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'numero', 'ano')
    search_fields = ('descricao', 'numero', 'ano',)
    list_filter = ('ano',)
    list_per_page = 20
    filter_horizontal = ('arquivos',)

    class Media:
      js = [
          '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
          '/static/grappelli/tinymce_setup/tinymce_setup.js',
      ]

