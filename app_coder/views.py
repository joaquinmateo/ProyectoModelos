from django.shortcuts import render
#Para tener la función Curso la importo de .models
from .models import Curso
#Para convertir la función en HTML debo agregar esto también
from django.http import HttpResponse

# Create your views here.
def crea_curso(req, nombre, camada):
    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"""
        <p>Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado con éxito</p>
    """)
#Esto lo agregamos a urls.py en urlspatterns

def lista_cursos(req):
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos": lista})
    #Dentro de la carpeta general debo crear un archivo html para que se muestre que se llame templates/(nombre).html

#Una vez creada las funciones vamos a models.py a crear las clases

def inicio(req):
    return render(req, "inicio.html", {})
def cursos(req):
    return render(req, "cursos.html", {})
def profesores(req):
    return render(req, "profesores.html", {})
def estudiantes(req):
    return render(req, "estudiantes.html", {})
def entregables(req):
    return render(req, "entregables.html", {})
#Vamos a hacer URLS organizadas, copiando las urls en app_coder