from django.views.generic import ListView, DetailView
from .models import EmendaParlamentar


class EmendaParlamentarListView(ListView):
    model = EmendaParlamentar
    template_name = 'emendas/emendas.html'
    context_object_name = 'emendas'
    queryset = EmendaParlamentar.objects.all()


class EmendaParlamentarDetailView(DetailView):
    model = EmendaParlamentar
    template_name = 'emendas/detail.html'
    context_object_name = 'emenda'




