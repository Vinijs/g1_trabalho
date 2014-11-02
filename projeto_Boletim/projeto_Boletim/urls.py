from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^$', 'usuarios.views.index'),
    url(r'^validar/$', 'usuarios.views.validar'), 
)
