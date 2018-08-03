from django.views.generic import ListView, TemplateView

from home.models import Noticia, BannerHome
from galeria.models import Galeria
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class InfraestruturaMixin(object):
    def get_context_data(self, **kwargs):
        context = super(InfraestruturaMixin, self).get_context_data(**kwargs)
        context["galeria_infra"] = Galeria.objects.select_related().filter(secretaria='infraestrutura').filter(secao='galeria2')[:1]
        context["banner337x280_infra"] = BannerHome.publicado.filter(secretaria='infraestrutura').filter(secao='banner_337x280')[:1]
        return context


class InfraestruturaNoticiaView(ComunsNoticiasMixin, InfraestruturaMixin, ListView):
    model = Noticia
    template_name = "infraestrutura/secretaria/noticias.html"
    paginate_by = 3
    context_object_name = 'infraestrutura_noticias'
    queryset = Noticia.publicado.filter(secretaria__exact='infraestrutura')[:50]


class InfraestruraHomeView(ComunsNoticiasMixin, InfraestruturaMixin, TemplateView):
    template_name = 'infraestrutura/secretaria/home.html'


class InfraestruturaSecretarioView(ComunsNoticiasMixin, InfraestruturaMixin, TemplateView):
    template_name = 'infraestrutura/secretaria/secretario.html'


class DAESView(ComunsNoticiasMixin, InfraestruturaMixin, TemplateView):
    template_name = 'infraestrutura/daes/daes.html'


class InfraestruturaLocalizacaoList(ComunsNoticiasMixin, InfraestruturaMixin, ListView):
    model = Localizacao
    template_name = "infraestrutura/localizacao/localizacao.html"
    context_object_name = "infraestrutura_localizacao_view"
    queryset = Localizacao.objects.all().filter(secretaria__exact='infraestrutura')

