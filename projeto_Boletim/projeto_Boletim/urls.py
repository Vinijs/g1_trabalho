from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuarios.views',
                       
    url(r'^$', 'index'),
    url(r'^login/$', 'login'),
    url(r'^validar/$', 'validar'),
    url(r'^logoff/$', 'logoff'),
    url(r'^dashboard/$', 'dashboard'),
    url(r'^inicio/$', 'inicio'),
    url(r'^notas/$', 'notas'),
    url(r'^provas/$', 'provas'),
    url(r'^horarios/$', 'horarios'),
    url(r'^biblioteca/$', 'biblioteca'),
    url(r'^cursos/$', 'cursos'),
    url(r'^avisos/$', 'avisos'),
    url(r'^cadastro/$', 'cadastro'),
    
   
                       
    url(r'^cadastro_validar/$', 'cadastro_validar'),
    url(r'^token/(?P<numero>\d+)/$', 'token'),
                       
    url(r'^i18n/', include('django.conf.urls.i18n')),#fazer uma rota para alterar a lingua coloquei i18n mas pode colocar o nome que quiser
     
)
