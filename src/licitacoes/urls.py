from django.conf.urls import url
from .views import LicitacaoListView, LicitacaoDetailView, ModalidadeListView


urlpatterns = [
    url(r'^$', ModalidadeListView.as_view(), name='modalidade_view'),
    url(r'^lista/$', LicitacaoListView.as_view(), name='licitacao_view'),

    url(r'^(?P<pk>[\-\d\w]+)/$', LicitacaoDetailView.as_view(), name='licitacao_detalhe_view'),

]
