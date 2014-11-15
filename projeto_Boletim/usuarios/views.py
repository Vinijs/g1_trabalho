from django.shortcuts import render, HttpResponseRedirect
from usuarios.forms import UsuarioForm, LoginForm, cadastroForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

def index(request):
    recado = _('Ola, Voce esta no site certo!')
    return render(request, 'index.html',{'recado':recado,})

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def validar(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            usuario = authenticate(username=form.data['login'], password=form.data['senha'])
            
            if usuario is not None:
                  if usuario.is_active:
                    meu_login(request, usuario)
                    return HttpResponseRedirect('/dashboard/')
                  else:
                          return render(request, 'login.html',{'form' : form})
            else:
                return render(request, 'login.html',{'form' : form})
        else:
                return render(request, 'login.html',{'form': form})      
    else:
            return HttpResponseRedirect('/login/')
          
def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')
  
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

def cadastro(request):
    form = cadastroForm()
    return render(request, 'cadastro.html',{'form': form})

def cadastro_validar(request):
    if request.method == 'POST':
        form = cadastroForm(request.POST)
        
        if form.is_valid():
            usuario = Usuario(
            username=form.data['login'],
            email=form.data['email'],
            is_active=False
        )
        usuario.set_password(form.data['senha'])
        usuario.save()
        
        if send_mail('Campo assunto Aqui', 'Valide o seu email: http://unifran-78230.sae1.nitrousbox.com/token/'+str(usuario.pk), 'testeunifran@bol.com.br',
   [usuario.email], fail_silently=True):
            # Se der erro ele avisa aqui.
            # Retornar tela de sucesso! Vc Consegue fazer e tb arrumar esses codigos?
            return render(request,'cadastro.html',{'form':form})
        return render(request,'index.html',{'form':form})

def token(request, numero):
    usuario = Pessoa.objects.get(pk=numero)
    usuario.is_active = True
    usuario.save()
    return HttpResponseRedirect('/login/')




