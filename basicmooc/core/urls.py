from django.conf.urls import url

from simplemooc.core.views import home, contact

urlpatterns = [
    url('^$', home, name='home'),
    url('^contato/$', contact, name='contact')
]