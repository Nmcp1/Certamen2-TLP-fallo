from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicador, Entidad
# Create your views here.

def ordenador(request):
    entidades = Entidad.objects.all()
    comunicadores = Comunicador.objects.all()
    entidad_seleccionada = request.GET.get("entidad")

    if (entidad_seleccionada == "Todos" or entidad_seleccionada==None):
        comunicadores = Comunicador.objects.all()
    else:
        entidad_nueva = Entidad.objects.get(nombre=entidad_seleccionada)
        comunicadores = Comunicador.objects.filter(entidad=entidad_nueva)

    data ={
        "comunicados":comunicadores.order_by('-fecha_publicacion'),
        "entidades":entidades,
        "entidad_seleccionada":entidad_seleccionada
    }
    return render(request,'miapp/base.html',data)

def pantalla(request):
    comunicadores = Comunicador.objects.all()
    entidades = Entidad.objects.all()

    data ={
        "comunicados":comunicadores,
        "entidades":entidades,
    }
    return render(request,'miapp/pantalla.html',data)

def celular(request):
    comunicadores = Comunicador.objects.all()
    entidades = Entidad.objects.all()

    entidad_seleccionada = request.GET.get("entidad")

    if (entidad_seleccionada == "Todos" or entidad_seleccionada==None):
        comunicadores = Comunicador.objects.all()
    else:
        entidad_nueva = Entidad.objects.get(nombre=entidad_seleccionada)
        comunicadores = Comunicador.objects.filter(entidad=entidad_nueva)

    data ={
        "comunicados":comunicadores.order_by('-fecha_publicacion'),
        "entidades":entidades,
        "entidad_seleccionada":entidad_seleccionada
    }
    return render(request,'miapp/celular.html',data)

def inicio(request):
    return render(request,'miapp/inicio.html')

def base(request):
    entidades = Entidad.objects.all()
    comunicadores = Comunicador.objects.all()
    entidad_seleccionada = request.GET.get("entidad")

    if (entidad_seleccionada == "Todos" or entidad_seleccionada==None):
        comunicadores = Comunicador.objects.all()
    else:
        entidad_nueva = Entidad.objects.get(nombre=entidad_seleccionada)
        comunicadores = Comunicador.objects.filter(entidad=entidad_nueva)

    data ={
        "comunicados":comunicadores.order_by('-fecha_publicacion'),
        "entidades":entidades,
        "entidad_seleccionada":entidad_seleccionada
    }
    return render(request,'miapp/base.html',data)    