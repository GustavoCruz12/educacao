from django.views.generic import ListView, TemplateView

from home.models import Noticia, BannerHome
from galeria.models import Galeria
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class CETMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CETMixin, self).get_context_data(**kwargs)
        context["galeria_cet"] = Galeria.objects.select_related().filter(secretaria='esportes').filter(secao='galeria2')[:1]
        context["banner337x280_esportes"] = BannerHome.publicado.filter(secretaria='esportes').filter(secao='banner_337x280')[:1]
        return context


class CETNoticiaView(ComunsNoticiasMixin, CETMixin, ListView):
    model = Noticia
    template_name = "esportes/secretaria/noticias.html"
    paginate_by = 3
    context_object_name = 'esporte_noticias'
    queryset = Noticia.publicado.filter(secretaria__exact='esportes')[:50]


class InfraestruraHomeView(ComunsNoticiasMixin, CETMixin, TemplateView):
    template_name = 'esportes/secretaria/home.html'


class CETSecretarioView(ComunsNoticiasMixin, CETMixin, TemplateView):
    template_name = 'esportes/secretaria/secretario.html'


class CETLocalizacaoList(ComunsNoticiasMixin, CETMixin, ListView):
    model = Localizacao
    template_name = "esportes/localizacao/localizacao.html"
    context_object_name = "esporte_localizacao_view"
    queryset = Localizacao.objects.all().filter(secretaria__exact='esportes')