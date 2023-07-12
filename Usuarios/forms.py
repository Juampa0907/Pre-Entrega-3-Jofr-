from django import forms
from .models import *

#estuve teniendo problemas porque algunos elementos como 
#TextField no me lo tomaaba en forms, entonces encontré que se pueden
#crear formularios a partir de los modelos  con forms.ModelForm

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        #uso el labels para darle nombres lógicos a los formularios
        # por ejemplo que sea Contraseña y contrasena
        labels = {
            'nombre':'Nombre',
            'email':'Correo Electrónico',
            'contrasena': 'Contraseña',
            'nomusu': 'Nombre de Usuario',

        }

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'  
        labels = {
            'nombre': 'Nombre del videojuego',
            'ano_lanzamiento': 'Año de lanzamiento',
            'genero': 'Género',
            'desarrollador': 'Desarrollador',
            'plataforma': 'Plataforma',
            'descripcion': 'Descripción',
            'requisitos_sistema': 'Requisitos del sistema',
        }

class RecomendacionForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = '__all__'  
        labels = {
            'usuario': 'Usuario',
            'videojuego': 'Videojuego',
            'comentario': 'Comentario',
            'fecha': 'Fecha',
            'puntuacion': 'Puntuación',
        }