from django.conf.urls import url

from .views import (
    EmpresaListView,
    VTNView,
    AdministracaoNoticiaView,
    AdministracaoHomeView,
    AdministracaoSecretarioView,
    AdministracaoLocalizacaoList,
    WebCidadaoView,
)


urlpatterns = [
    # home
    url(r'^$', AdministracaoHomeView.as_view(), name='administracao_view'),


    url(r'^empresa/$', EmpresaListView.as_view(), name='empresa'),
    url(r'^vtn/$', VTNView.as_view(), name='empresa_vtn'),
    url(r'^noticias/$', AdministracaoNoticiaView.as_view(), name='administracao_noticia'),
    url(r'^secretario/$', AdministracaoSecretarioView.as_view(), name='administracao_secretario'),
    url(r'^localizacao/$', AdministracaoLocalizacaoList.as_view(), name='administracao_localizacao'),
    url(r'^cidadao/$', WebCidadaoView.as_view(), name='administracao_cidadao'),

]
