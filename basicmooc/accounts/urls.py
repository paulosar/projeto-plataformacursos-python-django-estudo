from django.conf.urls import url
from django.contrib.auth import views as auth_views
from simplemooc.accounts.views import register, edit, dashboard, edit_password, password_reset, password_reset_confirm

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', auth_views.login, {'template_name':'accounts/login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout, {'next_page':'core:home'}, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
]