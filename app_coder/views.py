from django.shortcuts import render
#Para tener la función Curso la importo de .models
from .models import Curso, Profesor
#Para convertir la función en HTML debo agregar esto también
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

#Decorador
from django.contrib.auth.decorators import login_required #Este es para las funciones
#IMPORTANTE, PARA QUE ESTO FUNCIONE HAY QUE CAMBIAR EN settings.py y agregar LOGIN_URL = '/app-coder/login'
from django.contrib.auth.mixins import LoginRequiredMixin #Este es para las clases

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
    
def busqueda_camada(req):
    
    return render(req, "busqueda_camada.html") #lo agregamos a urls.py

def buscar_camada(req):

    num_camada = req.GET["camada"]

    cursos = Curso.objects.filter(camada__icontains=num_camada) #Ahora interactua con la base de datos, filter permite trabajar con más de un objeto e icontains hace una busqueda aproximada

    return render(req, "resultado_busqueda.html", { "cursos": cursos, "camada": num_camada}) #Creamos el template

@login_required #De ésta manera es necesario loguearse para ver ésta funión
def lista_profesores(req):
    profesores = Profesor.objects.all()

    return render(req, "leer_profesores.html", { "profesores": profesores }) #Read del CRUD

def crea_profesores(req):

    if req.method == 'POST':

        mi_formulario = ProfesorFormulario(req.POST)

        print(mi_formulario)

        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            nuevo_profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"] )
            nuevo_profesor.save()

            return HttpResponseRedirect('/app-coder')
        else:   
            return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario})
    
    else:

        mi_formulario = ProfesorFormulario()
        return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario}) 
    
def eliminar_profesor(req, id):
    
    if req.method == 'POST':

        profesor = Profesor.objects.get(id=id)
        profesor.delete()

        profesores = Profesor.objects.all()

        return render(req, "leer_profesores.html", { "profesores": profesores })
    
def editar_profesor(req, id):

    profesor = Profesor.objects.get(id=id)

    if req.method == 'POST':

        mi_formulario = ProfesorFormulario(req.POST)
        
        
        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]
            
            profesor.save()
            
            return HttpResponseRedirect('/app-coder')
        
        else:   
            
            return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario})
             

    else:

        mi_formulario = ProfesorFormulario(initial={
            "nombre":profesor.nombre,
            "apellido":profesor.apellido,
            "email":profesor.email,
            "profesion":profesor.profesion,
        })
        
        return render(req, "editar_profesor.html", { "mi_formulario": mi_formulario, "id": profesor.id}) 

#Vistas basadas en clases 

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso_list.html'
    context_object_name = 'cursos'

class CursoDetail(DetailView):
    model=Curso
    template_name = 'curso_detail.html'
    context_object_name = 'curso'

class CursoCreate(CreateView):
    model=Curso
    template_name = 'curso_create.html'
    fields = ['nombre', 'camada'] #Se puede usar __all__
    success_url = '/app-coder'

class CursoUpdate(UpdateView):
    model=Curso
    template_name= 'curso_update.html'
    fields=['nombre', 'camada']
    success_url= '/app-coder'
    context_object_name= 'curso'

class CursoDelete(DeleteView):
    model=Curso
    template_name= 'curso_delete.html'
    success_url= '/app-coder'
    context_object_name= 'curso'

#LOGIN

def login_view(req):
    if req.method == 'POST':

        mi_formulario = AuthenticationForm(req, data=req.POST)
        
        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", { "mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html", { "mensaje": f"Datos incorretos!"})
            
            return HttpResponseRedirect('/app-coder')
        
        else:   
            
            return render(req, "login.html", { "mi_formulario": mi_formulario }) 
             

    else:

        mi_formulario = AuthenticationForm()
        
        return render(req, "login.html", { "mi_formulario": mi_formulario }) 

def register(req):
    if req.method == 'POST':

        mi_formulario = UserCreationForm(req.POST)
        
        if mi_formulario.is_valid(): 

            data = mi_formulario.cleaned_data    

            usuario = data['username']

            mi_formulario.save()

            return render(req, "inicio.html", { "mensaje": f"Bienvenido {usuario} creado exitosamente!"})
            
        else:
            return render(req, "registro.html", { "mi_formulario": mi_formulario }) 
   
    else:

        mi_formulario = UserCreationForm()
        
        return render(req, "registro.html", { "mi_formulario": mi_formulario }) 