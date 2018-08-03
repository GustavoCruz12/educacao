from django.contrib import admin
from eventos.models import AgendaEventos


@admin.register(AgendaEventos)
class EventosAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('titulo', 'data_evento')
    date_hierarchy = 'data_evento'
    search_fields = ('titulo', 'data_evento')
    prepopulated_fields = {"slug": ("titulo",)}
    list_per_page = 20

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]

