"""urlconf for the layout application"""

from django.conf.urls import url
from .views import ContactView


urlpatterns =[
    url(r'^$', ContactView.as_view(), name='contato_view'),
]
