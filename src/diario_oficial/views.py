from django.views.generic import ListView
from datetime import date

from .models import DiarioOficial, DiarioOficialExtraArquivos

from utils.mixinscomuns import ComunsNoticiasMixin


class DiarioOficialsListView(ComunsNoticiasMixin, ListView):
    model = DiarioOficial
    template_name = 'diario_oficial/diario_oficial.html'
    context_object_name = 'diario_oficial'

    def get_context_data(self, **kwargs):
        context = super(DiarioOficialsListView, self).get_context_data(**kwargs)
        context["ano"] = DiarioOficial.objects.values('ano').distinct().order_by('-ano')
        context["mes"] = DiarioOficial.objects.values('mes').distinct().order_by('-mes')
        today = date.today()
        context["hoje"] = DiarioOficial.objects.filter(publicacao=today)
        context["arquivos_extra"] = DiarioOficialExtraArquivos.objects.all()

        return context


class BuscaDiarioOficialListView(ComunsNoticiasMixin, ListView):
    model = DiarioOficial
    template_name = 'diario_oficial/busca_diario_oficial.html'
    context_object_name = 'buscao_diario_oficial'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(BuscaDiarioOficialListView, self).get_context_data(**kwargs)
        context["arquivos_extra"] = DiarioOficialExtraArquivos.objects.all()
        return context

    def get_queryset(self, **kwargs):
        numero = self.request.GET.get('num')
        ano = self.request.GET.get('an')
        mes = self.request.GET.get('me')
        data = self.request.GET.get('dat')
        termo = self.request.GET.get('termo')

        diarios_oficiais = DiarioOficial.objects.all().order_by('-numero')

        if numero:
            diarios_oficiais = diarios_oficiais.filter(numero=numero)
        if ano:
            diarios_oficiais = diarios_oficiais.filter(ano=ano)
        if mes:
            diarios_oficiais = diarios_oficiais.filter(mes=mes)
        if data:
            diarios_oficiais = diarios_oficiais.filter(publicacao=data)
        if termo:
            print(len(termo))
            diarios_oficiais = diarios_oficiais.filter(texto_arquivo_diario__icontains=termo)
        return diarios_oficiais

