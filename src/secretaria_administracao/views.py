from django.views.generic import ListView, TemplateView

from django.views.generic import ListView, DetailView, TemplateView

from home.models import Noticia, BannerHome
from galeria.models import Galeria
from .models import Empresa, ComunicadoEmpresa
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class AdministracaoMixin(object):
    def get_context_data(self, **kwargs):
        context = super(AdministracaoMixin, self).get_context_data(**kwargs)
        context["galeria_adm"] = Galeria.objects.select_related().filter(secretaria='administracao').filter(secao='galeria2')[:1]
        context["banner337x280_adm"] = BannerHome.publicado.filter(secretaria='administracao').filter(secao='banner_337x280')[:1]
        context["banner_729x90_footer"] = BannerHome.publicado.filter(secretaria='administracao').filter(secao='banner_729x90_footer')[:1]
        return context


class AdministracaoNoticiaView(ComunsNoticiasMixin, AdministracaoMixin, ListView):
    model = Noticia
    template_name = "administracao/secretaria/noticias.html"
    paginate_by = 6
    context_object_name = 'administracao_noticias'
    queryset = Noticia.publicado.filter(secretaria='administracao')[:50]


class EmpresaListView(ComunsNoticiasMixin, AdministracaoMixin, ListView):
    model = Empresa
    template_name = "administracao/empresa/empresa.html"
    context_object_name = 'empresas'

    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self).get_context_data(**kwargs)

        context["manual"] = Empresa.objects.select_related().filter(tipo=0)
        context["decreto"] = Empresa.objects.select_related().filter(tipo=1)
        context["normativa"] = Empresa.objects.select_related().filter(tipo=2)
        context["legislacao"] = Empresa.objects.select_related().filter(tipo=3)
        context["formulario"] = Empresa.objects.select_related().filter(tipo=4)
        context["aviso"] = ComunicadoEmpresa.objects.select_related()[:3]
        return context


class VTNView(ComunsNoticiasMixin, AdministracaoMixin, TemplateView):
    template_name = "administracao/empresa/vtn.html"


class AdministracaoHomeView(ComunsNoticiasMixin, AdministracaoMixin, TemplateView):
    template_name = 'administracao/secretaria/home.html'


class AdministracaoSecretarioView(ComunsNoticiasMixin, AdministracaoMixin, TemplateView):
    template_name = 'administracao/secretaria/secretario.html'


class AdministracaoLocalizacaoList(ComunsNoticiasMixin, AdministracaoMixin, ListView):
    model = Localizacao
    template_name = "administracao/localizacao/localizacao.html"
    context_object_name = "administracao_localizacao_view"
    queryset = Localizacao.objects.all().filter(secretaria__exact='administracao')


class WebCidadaoView(ComunsNoticiasMixin, AdministracaoMixin, TemplateView):
    template_name = 'administracao/cidadao/cidadao.html'

