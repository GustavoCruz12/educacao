from django.conf.urls import url

from .views import (
    CETNoticiaView,
    InfraestruraHomeView,
    CETSecretarioView,
    CETLocalizacaoList
)


urlpatterns = [
    # home
    url(r'^$', InfraestruraHomeView.as_view(), name='esporte'),
    url(r'^noticias/$',   CETNoticiaView.as_view(), name='esporte_noticia'),
    url(r'^secretario/$', CETSecretarioView.as_view(), name='esporte_secretario'),
    url(r'^localizacao/$',CETLocalizacaoList.as_view(), name='esporte_localizacao'),
]
