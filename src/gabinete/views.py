from django.views.generic import TemplateView

from home.models import Noticia, BannerHome
from galeria.models import Galeria
from utils.mixinscomuns import ComunsNoticiasMixin


class GabineteMixin(object):
    def get_context_data(self, **kwargs):
        context = super(GabineteMixin, self).get_context_data(**kwargs)
        context["galeria_adm"] = Galeria.objects.select_related().filter(secretaria='gabinete').filter(secao='galeria2')[:1]
        context["banner337x280_adm"] = BannerHome.publicado.filter(secretaria='gabinete').filter(secao='banner_337x280')[:1]
        return context


class PrefeitoTemplateView(ComunsNoticiasMixin, GabineteMixin, TemplateView):
    template_name = 'gabinete/prefeito.html'


class VicePrefeitoTemplateView(ComunsNoticiasMixin, GabineteMixin, TemplateView):
    template_name = 'gabinete/vice.html'

