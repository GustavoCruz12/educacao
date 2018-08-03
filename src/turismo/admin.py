from django.contrib import admin

from .models import Atracao, CategoriaAtracao, PontoTuristico


@admin.register(CategoriaAtracao)
class AdminCategoriaAtracao(admin.ModelAdmin):
    pass


@admin.register(Atracao)
class AdminAtracao(admin.ModelAdmin):
    pass


@admin.register(PontoTuristico)
class AdminPontoTuristico(admin.ModelAdmin):
    pass
