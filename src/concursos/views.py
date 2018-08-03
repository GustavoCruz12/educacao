from django.views.generic import ListView, DetailView

from .models import TipoConcurso, Concurso

from utils.mixinscomuns import ComunsNoticiasMixin


class TipoConcursoListView(ComunsNoticiasMixin, ListView):
    model = TipoConcurso
    template_name = "concursos/tipo_concurso.html"
    context_object_name = 'tipo_concurso'

    def get_context_data(self, **kwargs):
        context = super(TipoConcursoListView, self).get_context_data(**kwargs)
        context["tipo"] = TipoConcurso.objects.select_related().order_by('descricao')
        context["ano"] = Concurso.objects.values('ano').distinct().order_by('-ano')
        return context


class ConcursoListView(ComunsNoticiasMixin, ListView):
    model = Concurso
    template_name = "concursos/concurso.html"
    context_object_name = 'concurso'

    def get_queryset(self, **kwargs):

        tipo = self.request.GET.get('t')
        ano = self.request.GET.get('a')

        resultado = Concurso.objects.select_related().order_by('-ano', '-numero')

        if tipo:
            resultado = resultado.filter(tipo=tipo)
        if ano:
            resultado = resultado.filter(ano=ano)
        return resultado


class ConcursoDetailView(ComunsNoticiasMixin, DetailView):
    model = Concurso
    template_name = "concursos/concurso_detalhe.html"
    context_object_name = "concurso_detalhe"

