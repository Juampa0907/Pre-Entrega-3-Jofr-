from django.urls import path
from Usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('prueba/', views.prueba, name='prueba' ),
    path('anadir-videojuego/', views.anadir_videojuego, name='anadir_videojuego'),
    path('crear-recomendacion/', views.crear_recomendacion, name='crear_recomendacion'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    #path('busqueda_recomendacion', views.busqueda_recomendacion, name='busqueda_recomendacion'),
    path('buscar/', views.buscar, name='buscar'),
    path('ultimas-recomendaciones/', views.ultimas_recomendaciones, name='ultimas_recomendaciones'),
    path('ultimos-videojuegos/', views.ultimos_videojuegos, name='ultimos_videojuegos'),
    path('buscar_juego/', views.buscar_juego, name='buscar_juego'),
]
