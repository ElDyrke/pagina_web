from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidoP=models.CharField(max_length=30)
    apellidoM=models.CharField(max_length=30)
    emaiil=models.EmailField(unique=True)
    UserName = models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)