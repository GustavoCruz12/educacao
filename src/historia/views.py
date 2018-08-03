from django.views.generic import TemplateView
from utils.mixinscomuns import ComunsNoticiasMixin


class DadosSerranaView(ComunsNoticiasMixin, TemplateView):
    template_name = 'serrana/dados.html'


class HistoriaSerranaView(ComunsNoticiasMixin, TemplateView):
    template_name = 'serrana/historia.html'


class HinoSerranaView(ComunsNoticiasMixin, TemplateView):
    template_name = 'serrana/hino.html'


class PrefeitosSerranaView(ComunsNoticiasMixin, TemplateView):
    template_name = 'serrana/prefeitos.html'


class HojeSerranaView(ComunsNoticiasMixin, TemplateView):
    template_name = 'serrana/hoje.html'

