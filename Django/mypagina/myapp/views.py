from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Usuario

# Create your views here.
# class Usuario(models.Model):
#     nombre = models.CharField(max_length=30)
#     apellidoP=models.CharField(max_length=30)
#     apellidoM=models.CharField(max_length=30)
#     emaiil=models.EmailField(unique=True)
#     UserName = models.CharField(max_length=30)
#     contraseña=models.CharField(max_length=30)

def inicio(request):
    template = loader.get_template("inicio.html")
    return HttpResponse(template.render())

def formulario(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellidoP = request.POST["apellidoP"]
        apellidoM = request.POST["apellidoM"]
        email = request.POST["emaiil"]
        userName = request.POST["UserName"]
        contrasena = request.POST["contrasena"]

        user = Usuario(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, emaiil=email, UserName=userName, contrasena=contrasena)
        user.save()

        return render(request, 'inicio.html')

    return render(request, 'form.html')

def login(request):

    if request.method == "POST":

        userName = request.POST["UserName"]
        contrasena = request.POST["contrasena"]

        user = Usuario.objects.get(userName = userName)

        if user == None:
            return(request, 'login.html', {"error" : "usrname"})
        elif user.contrasena == contrasena:
            return render(request, 'inicio.html', {"user":user})
        else:
            return(request, 'login.html', {"error" : "psswrd"})

    return render(request, 'login.html')


def perfilUsuario(request):
    
    return render(request, 'perfil.html')