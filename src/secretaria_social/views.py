from django.views.generic import ListView, TemplateView

from home.models import Noticia, BannerHome
from galeria.models import Galeria
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class SocialMixin(object):
    def get_context_data(self, **kwargs):
        context = super(SocialMixin, self).get_context_data(**kwargs)
        context["galeria_social"] = Galeria.objects.select_related().filter(secretaria='social').filter(secao='galeria2')[:1]
        context["banner337x280_social"] = BannerHome.publicado.filter(secretaria='social').filter(secao='banner_337x280')[:1]
        return context


class SocialNoticiaView(ComunsNoticiasMixin, SocialMixin, ListView):
    model = Noticia
    template_name = "social/secretaria/noticias.html"
    paginate_by = 3
    context_object_name = 'social_noticias'
    queryset = Noticia.publicado.filter(secretaria__exact='social')[:50]


class InfraestruraHomeView(ComunsNoticiasMixin, SocialMixin, TemplateView):
    template_name = 'social/secretaria/home.html'


class SocialSecretarioView(ComunsNoticiasMixin, SocialMixin, TemplateView):
    template_name = 'social/secretaria/secretario.html'


class SocialLocalizacaoList(ComunsNoticiasMixin, SocialMixin, ListView):
    model = Localizacao
    template_name = "social/localizacao/localizacao.html"
    context_object_name = "social_localizacao_view"
    queryset = Localizacao.objects.all().filter(secretaria__exact='social')

