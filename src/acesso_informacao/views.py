from django.shortcuts import render

from django.views.generic import TemplateView

from utils.mixinscomuns import ComunsNoticiasMixin


class AcessoInformacaoTemplateView(ComunsNoticiasMixin,TemplateView):
    template_name = 'acesso_informacao/acesso_informacao.html'

