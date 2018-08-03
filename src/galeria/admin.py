from django.contrib import admin
from .models import Galeria, FotoGaleria


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('titulo', 'publicacao')
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 20


@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('titulo', 'imagem', 'publicacao')
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 20
