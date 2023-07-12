from django.shortcuts import render
from Usuarios.forms import *
from Usuarios.models import *
from django.http import *

def inicio(request):
    return render(request, 'Usuarios/inicio.html')


def prueba(request):
    return render(request, 'Usuarios/prueba.html')


def crear_usuario(request):
    if request.method == 'POST':
        miFormulario = UsuariosForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            
            return render(request, 'Usuarios/inicio.html')
    else:
        miFormulario = UsuariosForm()
    return render(request, 'Usuarios/crear_usuario.html', {'miFormulario': miFormulario})


def anadir_videojuego(request):
    if request.method == 'POST':
        miFormulario = VideojuegoForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            # Hacer algo con el objeto videojuego creado
            return render(request, 'Usuarios/inicio.html')
    else:
        miFormulario = VideojuegoForm()
    return render(request, 'Usuarios/anadir_videojuego.html', {'miFormulario':miFormulario})

def crear_recomendacion(request):
    if request.method == 'POST':
        miFormulario = RecomendacionForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            # Hacer algo con el objeto recomendacion creado
            return render(request, 'Usuarios/inicio.html')
    else:
        miFormulario = RecomendacionForm()
    return render(request, 'Usuarios/crear_recomendacion.html', {'miFormulario': miFormulario})


#estaba usando la funcion de abajao, pero obtuve un botón el cual lo
#pude hacer que funcione como buscador a traves de un metodo get y 
#asi enviarle la informacion a la funcion buscar

#def busqueda_recomendacion(request):
#    return render(request,'Usuarios/busqueda_recomendacion.html')

def buscar(request):
    if request.GET.get('videojuego'):
        videojuego_busqueda = request.GET.get('videojuego')
        resultados = Recomendacion.objects.filter(videojuego__nombre__icontains=videojuego_busqueda)
        return render(request, 'Usuarios/resultados_busqueda.html', {"resultados": resultados, "videojuego_busqueda": videojuego_busqueda})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
#icontains me daba un error con el tema de las foreign keys, por eso uso __icontains que entiendo que hace una busqueda parcial

def ultimas_recomendaciones(request):
    ultimas_recomendaciones = Recomendacion.objects.order_by('-fecha')[:3]

    context = {
        'ultimas_recomendaciones': ultimas_recomendaciones
    }

    return render(request, 'Usuarios/ultimas_recomendaciones.html', context)

def ultimos_videojuegos(request):
    ultimos_videojuegos=Videojuego.objects.order_by('-plataforma')[:3]

    context = {
        'ultimos_videojuegos': ultimos_videojuegos
    }

    return render(request, 'Usuarios/ultimos_videojuegos.html', context)


def buscar_juego(request):
    if request.GET.get('videojuego'):
        videojuego_busqueda = request.GET.get('videojuego')
        resultados = Videojuego.objects.filter(nombre__icontains=videojuego_busqueda)
        return render(request, 'Usuarios/resultados_busqueda_videojuegos.html', {"resultados": resultados, "videojuego_busqueda": videojuego_busqueda})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
