from django.contrib import admin
from leis.models import Lei


@admin.register(Lei)
class LeiAdmin(admin.ModelAdmin):
    list_display = ('tipo_lei', 'numero', 'titulo', 'ano')
    list_filter = ('ano', 'tipo_lei')
    search_fields = ('titulo', 'numero')
    list_per_page = 20
