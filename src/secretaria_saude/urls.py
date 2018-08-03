from django.conf.urls import url
from .views import (
    SaudeView,
    SaudeEscalaList,
    SaudeEscalaDetail,
    SaudeMedicamentoList,
    SaudeNoticiaView,
    SaudeSecretarioView,
    SaudeLocalizacaoList
)


urlpatterns = [
    # home
    url(r'^$', SaudeView.as_view(), name='saude_view'),

    # escalas
    url(r'^escalas/$', SaudeEscalaList.as_view(), name='saude_escala_list_view'),
    url(r'^escala/detail/(?P<pk>[\-\d\w]+)/$', SaudeEscalaDetail.as_view(), name='saude_escala_detail_view'),
    url(r'^medicamentos/$', SaudeMedicamentoList.as_view(), name='saude_medicamento_url'),
    url(r'^noticias/$', SaudeNoticiaView.as_view(), name='saude_noticia_url'),
    url(r'^secretario/$', SaudeSecretarioView.as_view(), name='saude_secretario'),
    url(r'^localizacao/$', SaudeLocalizacaoList.as_view(), name='saude_localizacao'),

]
