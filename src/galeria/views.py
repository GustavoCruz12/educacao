from django.views.generic import ListView, DetailView
from .models import Galeria
from utils.mixinscomuns import ComunsNoticiasMixin


class GaleriaListView(ComunsNoticiasMixin, ListView):
    model = Galeria
    template_name = "galerias/galeria_list.html"
    paginate_by = 9
    context_object_name = 'list_galerias'
    queryset = Galeria.objects.select_related()


class GaleriaDetailView(ComunsNoticiasMixin, DetailView):
    model = Galeria
    template_name = 'galerias/galeria_detail.html'
    context_object_name = 'galeria'

