from django.shortcuts import render
from django.views.generic.list import ListView
from .models import (Crianca,)


class CriancaList(ListView):
    model = Crianca
    template_name = 'crianca/PaginaInicial.html'
    context_object_name = 'criancas'
    queryset = Crianca.objects.all()


class CriancaListSearch(ListView):
    model = Crianca
    template_name = 'crianca/PaginaPesquisa.html'
    context_object_name = 'criancas'
    queryset = Crianca.objects.all()

    def get_queryset(self, **kwargs):
        crianca = Crianca.objects.all()
        search = self.request.GET.get('search_box')

        if search is not None:
            crianca = crianca.filter(nome_crianca__icontains=search)
            return crianca
