from django.db import models

class Usuarios(models.Model):
    nombre=models.CharField(max_length=30)
    nomusu= models.CharField(max_length=20)
    contrasena= models.CharField(max_length=20)
    email=models.EmailField()


