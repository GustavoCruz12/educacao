from django.conf.urls import url
from .views import DiarioOficialsListView, BuscaDiarioOficialListView


urlpatterns = [
    # leis
    url(r'^$', DiarioOficialsListView.as_view(), name='diario_view'),

    # busca lei
    url(r'^busca-diario/$', BuscaDiarioOficialListView.as_view(), name='busca_diario_view'),

]

# 9.0.1.71 apps
