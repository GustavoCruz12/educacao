from django.contrib import admin

from .models import Atracao, CategoriaAtracao


@admin.register(CategoriaAtracao)
class AdminCategoriaAtracao(admin.ModelAdmin):
    pass


@admin.register(Atracao)
class AdminAtracao(admin.ModelAdmin):
    pass
