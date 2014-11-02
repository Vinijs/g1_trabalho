from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        
class UsuarioLogin(forms.Form):
    username = forms.CharField(max_length='30', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
          
