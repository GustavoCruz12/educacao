from django.shortcuts import render
from django.views.generic import TemplateView

from utils.mixinscomuns import ComunsNoticiasMixin


class TransparenciaView(ComunsNoticiasMixin, TemplateView):
    template_name = 'transparencia/transparencia.html'

