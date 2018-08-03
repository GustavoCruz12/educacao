from django.views.generic import TemplateView
from utils.mixinscomuns import ComunsNoticiasMixin


class ConsultaPublicaTemplateView(ComunsNoticiasMixin, TemplateView):
    template_name = 'consulta_publica/index.html'
