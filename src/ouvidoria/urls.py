from django.conf.urls import url

from .views import (
    OuvidoriaView,
    OuvidoriaHome
)


urlpatterns = [

    url(r'^sobre/$', OuvidoriaHome.as_view(), name='sobre'),
    url(r'^$', OuvidoriaView.as_view(), name='home'),

]
