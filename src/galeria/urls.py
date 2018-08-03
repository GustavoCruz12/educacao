"""urlconf for the layout application"""

from django.conf.urls import url
from .views import GaleriaListView, GaleriaDetailView


urlpatterns =[
    url(r'^$', GaleriaListView.as_view(), name='galeria_list'),
    url(r'^galeria/(?P<slug>[\-\d\w]+)/$', GaleriaDetailView.as_view(), name='galeria_detail'),

]
