from django.db import models

class Usuario(models.Model):
  
  nome = models.CharField(max_length=100)
  email = models.EmailField()
  senha = models.CharField(max_length=15)
  serie = models.CharField(max_length=10)
  

  

# Create your models here.
