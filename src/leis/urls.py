from django.conf.urls import url
from .views import LeisListView, BuscaLeiListView, LdoPpaLoaTemplateView


urlpatterns = [
    # leis
    url(r'^$', LeisListView.as_view(), name='leis_view'),

    # busca lei
    url(r'^busca-lei/$', BuscaLeiListView.as_view(), name='busca_lei_view'),

    # ldo/ppa/loa
    url(r'^ldo-loa-ppa/$', LdoPpaLoaTemplateView.as_view(), name='ldo_loa_ppa_view'),

]
