from django.conf.urls import url
from .views import LocalizacaoView, BuscaLlocalizacaoListView


urlpatterns = [
    # localização
    url(r'^$', LocalizacaoView.as_view(), name='localizacao_view'),

    # busca a localização
    url(r'^busca-localizacao/', BuscaLlocalizacaoListView.as_view(), name='busca_localizacao_view'),

]
