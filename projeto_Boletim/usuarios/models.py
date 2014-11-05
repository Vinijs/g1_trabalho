from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
  #username = models.CharField(max_length=50,blank=True,null= True)
  #email = models.EmailField()
  #password = forms.CharField(widget=forms.PasswordInput)
  endereco = models.CharField(max_length=100, blank=True, null = True)
  

  

# Create your models here.
