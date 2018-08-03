from django.conf.urls import url

from .views import (
    DadosSerranaView,
    HinoSerranaView,
    HistoriaSerranaView,
    PrefeitosSerranaView,
    HojeSerranaView
)


urlpatterns = [

    url(r'^$', DadosSerranaView.as_view(), name='dados'),
    url(r'^dados/$', DadosSerranaView.as_view(), name='dados'),
    url(r'^hino/$', HinoSerranaView.as_view(), name='hino'),
    url(r'^historia/$', HistoriaSerranaView.as_view(), name='historia'),
    url(r'^prefeitos/$', PrefeitosSerranaView.as_view(), name='prefeitos'),
    url(r'^hoje/$', HojeSerranaView.as_view(), name='hoje'),

]
