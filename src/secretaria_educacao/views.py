from django.views.generic import ListView, TemplateView

from home.models import Noticia, BannerHome
from galeria.models import Galeria
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class AdministracaoMixin(object):
    def get_context_data(self, **kwargs):
        context = super(AdministracaoMixin, self).get_context_data(**kwargs)
        context["galeria_educ"] = Galeria.objects.select_related().filter(secretaria='educacao').filter(secao='galeria2')[:1]
        context["banner337x280_educ"] = BannerHome.publicado.filter(secretaria='educacao').filter(secao='banner_337x280')[:1]
        return context


class EducacaoNoticiaView(ComunsNoticiasMixin, AdministracaoMixin, ListView):
    model = Noticia
    template_name = "educacao/secretaria/noticias.html"
    paginate_by = 3
    context_object_name = 'educacao_noticias'
    queryset = Noticia.publicado.filter(secretaria__exact='educacao')[:50]


class EducacaoHomeView(ComunsNoticiasMixin, AdministracaoMixin, TemplateView):
    template_name = 'educacao/secretaria/home.html'


class EducacaoSecretarioView(ComunsNoticiasMixin, AdministracaoMixin, TemplateView):
    template_name = 'educacao/secretaria/secretario.html'


class EducacaoLocalizacaoList(ComunsNoticiasMixin, AdministracaoMixin, ListView):
    model = Localizacao
    template_name = "educacao/localizacao/localizacao.html"
    context_object_name = "educacao_localizacao_view"
    queryset = Localizacao.objects.all().filter(secretaria__exact='educacao')

