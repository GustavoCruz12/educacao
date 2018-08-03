from django.views.generic import ListView, DetailView, TemplateView


from .models import SaudeEscala, SaudeMedicamento
from home.models import Noticia, BannerHome
from galeria.models import Galeria
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class SaudeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(SaudeMixin, self).get_context_data(**kwargs)
        context["galeria_saude"] = Galeria.objects.select_related().filter(secretaria='saude').filter(secao='galeria2')[:1]
        context["banner337x280_saude"] = BannerHome.publicado.filter(secretaria='saude').filter(secao='banner_337x280')[:1]
        context["banner729x90_saude"] = BannerHome.publicado.filter(secretaria='saude').filter(secao='banner729x90_footer')[:1]

        return context


class SaudeView(ComunsNoticiasMixin, SaudeMixin, TemplateView):
    template_name = 'saude/secretaria/home.html'


class SaudeSecretarioView(ComunsNoticiasMixin, SaudeMixin, TemplateView):
    template_name = 'saude/secretaria/secretario.html'


class SaudeNoticiaView(ComunsNoticiasMixin, SaudeMixin, ListView):
    model = Noticia
    template_name = "saude/secretaria/noticias.html"
    paginate_by = 6
    context_object_name = 'saude_noticias'
    queryset = Noticia.publicado.filter(secretaria='saude')[:50]


class SaudeEscalaList(ComunsNoticiasMixin, SaudeMixin, ListView):
    model = SaudeEscala
    template_name = "saude/escalas/escala.html"
    context_object_name = "saude_escala_view"
    queryset = SaudeEscala.objects.select_related()


class SaudeEscalaDetail(ComunsNoticiasMixin, SaudeMixin, DetailView):
    model = SaudeEscala
    template_name = "saude/escalas/escala_detail.html"
    context_object_name = "saude_escala_detalhe_view"


class SaudeMedicamentoList(ComunsNoticiasMixin, SaudeMixin, ListView):
    model = SaudeMedicamento
    template_name = "saude/medicamentos/saude_medicamentos.html"
    context_object_name = "saude_medicamentos_view"
    queryset = SaudeMedicamento.objects.all()[:2]


class SaudeLocalizacaoList(ComunsNoticiasMixin, SaudeMixin, ListView):
    model = Localizacao
    template_name = "saude/localizacao/localizacao.html"
    context_object_name = "saude_localizacao_view"
    queryset = Localizacao.objects.all().filter(secretaria__exact='saude')