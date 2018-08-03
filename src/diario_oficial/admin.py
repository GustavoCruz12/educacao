from django.contrib import admin
from .models import DiarioOficial, DiarioOficialExtraArquivos



class DiarioOficialExtraInLine(admin.StackedInline):
    model = DiarioOficialExtraArquivos
    extra = 0
    max_num = 1
    classes = ('grp-collapse grp-open',)
    #inline_classes = ('grp-collapse grp-open',)


@admin.register(DiarioOficial)
class LeiAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ano', 'mes', 'publicacao')
    list_filter = ('ano', 'mes')
    search_fields = ('ano', 'mes', 'publicacao')
    list_per_page = 20
    inlines = [
        DiarioOficialExtraInLine
    ]
