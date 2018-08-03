from django.views.generic import ListView
from localizacao_orgaos.models import Localizacao
from utils.mixinscomuns import ComunsNoticiasMixin


class LocalizacaoView(ComunsNoticiasMixin, ListView):
    model = Localizacao
    template_name = "localizacao/local.html"
    context_object_name = "localizacao"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(LocalizacaoView, self).get_context_data(**kwargs)
        context["secre"] = Localizacao.objects.values('secretaria').distinct().order_by('secretaria')
        return context


class BuscaLlocalizacaoListView(ComunsNoticiasMixin, ListView):
    model = Localizacao
    template_name = 'localizacao/busca-localizacao.html'
    context_object_name = 'busca_localizacao'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        secretaria = self.request.GET.get('secretaria')
        orgao = self.request.GET.get('orgao')
        endereco = self.request.GET.get('endereco')
        telefone = self.request.GET.get('telefone')

        localizacao = Localizacao.objects.all().order_by('orgao')

        if secretaria:
            localizacao = localizacao.filter(secretaria=secretaria)
        if orgao:
            localizacao = localizacao.filter(orgao__icontains=orgao)
        if endereco:
            localizacao = localizacao.filter(endereco__icontains=endereco)
        if telefone:
            localizacao = localizacao.filter(telefone__icontains=telefone)
        return localizacao

