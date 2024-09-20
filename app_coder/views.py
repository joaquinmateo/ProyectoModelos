from django.shortcuts import render
#Para tener la función Curso la importo de .models
from .models import Curso
#Para convertir la función en HTML debo agregar esto también
from django.http import HttpResponse
from .forms import CursoFormulario

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

#FORMULARIOS

def curso_formulario(req):

    print(req.method)
    print("Se ejecutó curso-formulario") 
    #Cada vez que se cargue la página con la URL curso-formulario, aparecerá éste mensaje en la terminal
    #Si además cargamos datos en el formulario, esos datos también aparecerán
    print('data', req.POST) #Querydict significa que entiende la data como un diccionario

    if req.method == 'POST':

        mi_formulario = CursoFormulario(req.POST) #Ahora lo que se produce, lo hace de forms.py

        print(mi_formulario)

        if mi_formulario.is_valid(): #Con esto podemos definir qué aceptamos o no para el formulario

            data = mi_formulario.cleaned_data    

            nuevo_curso = Curso(nombre=req.POST["curso"], camada=req.POST["camada"])
            nuevo_curso.save()

            return render(req, "inicio.html", {})
        else:   
            return render(req, "curso_formulario.html", { "mi_formulario": mi_formulario})
    
    else:

        #Ahora vamos a hacer un formulario pero de Django, no de HTML
        #En app_coder creamos el archivo forms.py

        mi_formulario = CursoFormulario()
        return render(req, "curso_formulario.html", { "mi_formulario": mi_formulario}) #Lo agregamos a urls.py
    
#Ahora vamos a hacer un formulario pero de Django, no de HTML
#En app_coder creamos el archivo forms.py

def busqueda_camada(req):
    return render(req, "busqueda_camada.html") #lo agregamos a urls.py

def buscar_camada(req):

    num_camada = req.GET["camada"]

    cursos = Curso.objects.filter(camada__icontains=num_camada) #Ahora interactua con la base de datos, filter permite trabajar con más de un objeto e icontains hace una busqueda aproximada

    return render(req, "resultado_busqueda.html", { "cursos": cursos, "camada": num_camada}) #Creamos el template