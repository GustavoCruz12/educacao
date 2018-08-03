from django.views.generic import ListView, TemplateView


from .models import Lei

from utils.mixinscomuns import ComunsNoticiasMixin


class LeisListView(ComunsNoticiasMixin, ListView):
    model = Lei
    template_name = 'leis/leis.html'
    context_object_name = 'leis'

    def get_context_data(self, **kwargs):
        context = super(LeisListView, self).get_context_data(**kwargs)
        context["an"] = Lei.objects.values('ano').distinct().order_by('-ano')
        context["tl"] = Lei.objects.values('tipo_lei').distinct().order_by('tipo_lei')
        return context


class BuscaLeiListView(ComunsNoticiasMixin, ListView):
    model = Lei
    template_name = 'leis/busca-leis.html'
    context_object_name = 'busca_leis'
    paginate_by = 50

    def get_queryset(self, **kwargs):
        numero = self.request.GET.get('n')
        ano = self.request.GET.get('a')
        tipo_lei = self.request.GET.get('t')
        palavra = self.request.GET.get('p')

        leis = Lei.objects.all().order_by('-numero')

        if numero:
            leis = leis.filter(numero=numero)
        if ano:
            leis = leis.filter(ano=ano)
        if tipo_lei:
            leis = leis.filter(tipo_lei=tipo_lei)
        if palavra:
            leis = leis.filter(titulo__icontains=palavra)
        return leis


class LdoPpaLoaTemplateView(ComunsNoticiasMixin, TemplateView):
    template_name = 'leis/ppa_ldo_loa.html'

