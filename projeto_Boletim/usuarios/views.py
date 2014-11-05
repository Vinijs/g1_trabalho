from django.shortcuts import render, HttpResponseRedirect
from usuarios.forms import UsuarioForm, LoginForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

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
           # usuario.save()
            
            #usuarios = Usuario.objects.all()
            
            #return render(request, 'validar.html', {'form' : form, 'usuarios' : usuarios })
def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')
  
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')
  
# Create your views here.
