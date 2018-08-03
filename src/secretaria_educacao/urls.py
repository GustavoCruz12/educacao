from django.conf.urls import url

from .views import (
    EducacaoNoticiaView,
    EducacaoHomeView,
    EducacaoSecretarioView,
    EducacaoLocalizacaoList
)


urlpatterns = [
    # home
    url(r'^$', EducacaoHomeView.as_view(), name='educacao'),
    url(r'^noticias/$', EducacaoNoticiaView.as_view(), name='educacao_noticia'),
    url(r'^secretario/$', EducacaoSecretarioView.as_view(), name='educacao_secretario'),
    url(r'^localizacao/$', EducacaoLocalizacaoList.as_view(), name='educacao_localizacao'),

]
