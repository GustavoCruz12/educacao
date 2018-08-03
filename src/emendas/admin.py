from django.contrib import admin
from .models import EmendaParlamentar


@admin.register(EmendaParlamentar)
class EmendaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('deputado', 'valor', 'destino', 'publicacao')
    list_filter = ('deputado',)
    search_fields = ('deputado', 'destino')
