from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

generos_choices = [
    ('accion', 'Acción'),
    ('aventura', 'Aventura'),
    ('rol', 'RPG'),
    ('estrategia', 'Estrategia'),
    ('deporte', 'Deporte'),
    ('disparos', 'Disparos'),
    ('plataformas', 'Plataformas'),
    ('simulacion', 'Simulación'),
    ('puzzle', 'Puzzle'),
] #lo agrego para que el usuario no tenga la opcion de "inventar"
#y solo pueda elegir opciones predeterminadas

class Usuarios(models.Model):
    nombre=models.CharField(max_length=30)
    nomusu= models.CharField(max_length=20)
    contrasena= models.CharField(max_length=20)
    email=models.EmailField()

    #si bien es algo que vimos la clase siguiente es algo que me sirve el str
    #para armar bien la recomendacion
    def __str__(self):
        return f"{self.nomusu}"

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    ano_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50, choices=generos_choices)
    desarrollador = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50)
    descripcion = models.TextField()
    requisitos_sistema = models.TextField()

    def __str__(self):
        return f"{self.nombre}"
    

#las foreignkeys las uso para que si se elimina el usuario que
#creó la recomendacion tambien se elimine la recomendacion
#lo mismo para con el videojuego

#ademas esto me sirve para decir que usuario crea tal recomendacion para tal videojuego

class Recomendacion(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    puntuacion = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])






