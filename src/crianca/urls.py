from django.conf.urls import url
from .views import CriancaList, CriancaListSearch


urlpatterns = [
    # leis
    url(r'^$', CriancaList.as_view(), name='crianca_list'),

    # busca lei
    url(r'^crianca-busca/$', CriancaListSearch.as_view(), name='crianca_list_search'),

]


