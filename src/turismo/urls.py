from django.conf.urls import url

from .views import turismo, pontos_turisticos


urlpatterns = [
    # home
    url(r'^$', turismo, name='turismo'),
    url(r'^pontos/$', pontos_turisticos, name='pontos_turisticos'),

]
