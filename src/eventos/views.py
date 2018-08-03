from django.views.generic import ListView, DetailView
from .models import AgendaEventos

from utils.mixinscomuns import ComunsNoticiasMixin


class AgendaEventosListView(ComunsNoticiasMixin, ListView):
    model = AgendaEventos
    template_name = "eventos/lista_eventos.html"
    queryset = AgendaEventos.objects.select_related()
    context_object_name = "lista_eventos"
    paginate_by = 9


class AgendaEventosDetailView(ComunsNoticiasMixin, DetailView):
    model = AgendaEventos
    template_name = "eventos/evento.html"
    context_object_name = "evento"