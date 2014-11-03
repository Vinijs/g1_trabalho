from django.conf.urls import patterns, include, url

teste

urlpatterns = patterns('',
    url(r'^$', 'usuarios.views.index'),
    url(r'^validar/$', 'usuarios.views.validar'), 
)
