from django.conf.urls import url

from .views import (
   GeolocalizacaoView
)


urlpatterns = [

    url(r'^mapa/$', GeolocalizacaoView.as_view(), name='mapa'),


]
