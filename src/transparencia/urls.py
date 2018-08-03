"""urlconf for the layout application"""

from django.conf.urls import url
from .views import TransparenciaView


urlpatterns =[
    url(r'^$', TransparenciaView.as_view(), name='transparencia_view'),
]
