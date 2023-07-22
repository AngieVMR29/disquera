from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request): #vista 1
    return HttpResponse("<h1>Bienvenido a la app</h1>")

def pagina1(request):
    return render(request,'views/pagina1.html')

def artista(request): #vista inicio artistas
     return render(request,'artistas/index.html')

def addartista(request):
    return render(request,'artistas/crear.html')

def editartista(request):
    return render(request, 'artistas/editar.html')


