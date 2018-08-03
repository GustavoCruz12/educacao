from django.conf.urls import url
from .views import (
    NoticiaListView,
    BuscaNoticiaListView
)


urlpatterns = [
    # home
    url(r'^$', NoticiaListView.as_view(), name='noticia_list'),
    url(r'^busca/', BuscaNoticiaListView.as_view(), name='noticia-busca'),

]
