from django.conf.urls import url

from .views import (
    InfraestruturaNoticiaView,
    InfraestruraHomeView,
   InfraestruturaSecretarioView,
    InfraestruturaLocalizacaoList,
    DAESView,
)


urlpatterns = [
    # home
    url(r'^$', InfraestruraHomeView.as_view(), name='infraestrutura'),
    url(r'^noticias/$', InfraestruturaNoticiaView.as_view(), name='infraestrutura_noticia'),
    url(r'^secretario/$', InfraestruturaSecretarioView.as_view(), name='infraestrutura_secretario'),
    url(r'^localizacao/$', InfraestruturaLocalizacaoList.as_view(), name='infraestrutura_localizacao'),
    url(r'^daes/$', DAESView.as_view(), name='infraestrutura_daes'),

]
