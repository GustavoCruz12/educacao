from django.views.generic import ListView, DetailView
from .models import ModalidadeLicitacao, Licitacao

from utils.mixinscomuns import ComunsNoticiasMixin


class ModalidadeListView(ComunsNoticiasMixin, ListView):
    model = ModalidadeLicitacao
    template_name = "licitacoes/modalidade.html"
    context_object_name = 'modalidade'

    def get_context_data(self, **kwargs):
        context = super(ModalidadeListView, self).get_context_data(**kwargs)
        context["mod"] = ModalidadeLicitacao.objects.select_related().order_by('descricao')
        context["ano"] = Licitacao.objects.values('ano').distinct().order_by('-ano')
        return context


class LicitacaoListView(ComunsNoticiasMixin, ListView):
    model = Licitacao
    template_name = "licitacoes/licitacao.html"
    context_object_name = 'lic'
    paginate_by = 15

    def get_queryset(self, **kwargs):

        modalidade = self.request.GET.get('m')
        ano = self.request.GET.get('a')

        resultado = Licitacao.objects.select_related().order_by('-ano', '-numero')

        if modalidade:
            resultado = resultado.filter(modalidade=modalidade)

        if ano:
            resultado = resultado.filter(ano=ano)

        return resultado


class LicitacaoDetailView(ComunsNoticiasMixin, DetailView):
    model = Licitacao
    template_name = "licitacoes/detalhe.html"
    context_object_name = "detalhe"
