from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
