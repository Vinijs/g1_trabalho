from django.shortcuts import render
from usuarios.forms import UsuarioForm, UsuarioLogin
from usuarios.models import Usuario

def index(request):
    form = UsuarioForm()
    return render(request, 'index.html', {'form' : form})
def validar(request):
  
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            usuario = Usuario(**form.cleaned_data)
            usuario.save()
            
            usuarios = Usuario.objects.all()
            
            return render(request, 'validar.html', {'form' : form, 'usuarios' : usuarios })
    
# Create your views here.
