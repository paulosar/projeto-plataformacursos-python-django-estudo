from django.conf.urls import url

from simplemooc.courses.views import index, details, enrollment, \
    announcements, undo_enrollment, show_announcement, lessons, lesson, material

urlpatterns = [
    url('^$', index, name='index'),
    url('^(?P<slug>[\w_-]+)/$', details, name='details'),
    url('^(?P<slug>[\w_-]+)/inscricao/$', enrollment, name='enrollment'),
    url('^(?P<slug>[\w_-]+)/anuncios/$', announcements, name='announcements'),
    url('^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', show_announcement, name='show_announcement'),
    url('^(?P<slug>[\w_-]+)/cancelar-inscricao/$', undo_enrollment, name='undo_enrollment'),
    url('^(?P<slug>[\w_-]+)/aulas/$', lessons, name='lessons'),
    url('^(?P<slug>[\w_-]+)/aula/(?P<pk>\d+)/$', lesson, name='lesson'),
    url('^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', material, name='material'),
]