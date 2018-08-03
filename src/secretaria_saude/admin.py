from django.contrib import admin
from .models import SaudeEscala, SaudeMedicamento


@admin.register(SaudeEscala)
class AdminSaudeEscala(admin.ModelAdmin):
    list_display = ('unidade', 'telefone', 'dt_atualizacao')


@admin.register(SaudeMedicamento)
class AdminSaudeMedicamentos(admin.ModelAdmin):
    pass
