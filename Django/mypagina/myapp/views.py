from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def inicio(request):
    template = loader.get_template("inicio.html")
    return HttpResponse(template.render())

def formulario(request):
    return render(request, 'form.html')

def perfilUsuario(request):
    
    return render(request, 'perfil.html')