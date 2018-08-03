import re
from django.db.models import Q
from django.utils.text import smart_split
from django.views.generic import ListView

from home.models import Noticia
from utils.mixinscomuns import ComunsNoticiasMixin


class NoticiaListView(ComunsNoticiasMixin, ListView):
    model = Noticia
    template_name = "noticias/noticia_list.html"
    paginate_by = 6
    context_object_name = 'list_noticias'
    queryset = Noticia.publicado.select_related()[:50]


class BuscaNoticiaListView(ComunsNoticiasMixin, ListView):
    model = Noticia
    template_name = 'noticias/busca-noticias.html'
    paginate_by = 7
    context_object_name = 'busca_noticias'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q', '')
        if query:
            querysets = []
            words = self._extract_terms(query)
            for word in words:
                querysets.append((
                    Q(titulo__icontains=word) |
                    Q(resumo__icontains=word) |
                    Q(secretaria__icontains=word) |
                    Q(conteudo__icontains=word)
                ))

            resultado = Noticia.objects.select_related().filter(*querysets)
        else:
            resultado = []

        return resultado

    def _extract_terms(self, query):
        return [self._clean_term(word) for word in smart_split(query)]

    def _clean_term(self, query):
        return re.sub('\,|\.|\"', '', query)

    def get_context_data(self, **kwargs):
        context = super(BuscaNoticiaListView, self).get_context_data(**kwargs)
        context['search_term'] = self.request.GET['q']
        return context

