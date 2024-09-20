
from django.urls import path
#debo importame las funciones de views
from .views import *

urlpatterns = [
    path('crea-curso', crea_curso),
    path('lista-cursos/', lista_cursos),
    path('profesores/', profesores, name = "Profesores"),
    path('cursos/', cursos, name = "Cursos"),
    path('estudiantes/', estudiantes, name = "Estudiantes"),
    path('entregables/', entregables, name = "Entregables"),
    path('', inicio),
    path('curso-formulario/', curso_formulario, name = "CursoFormulario"), #Creamos el template
    path('busqueda-camada/', busqueda_camada, name = "BusquedaCamada"), #Creamos el template
    path('buscar-camada/', buscar_camada, name = "BuscarCamada"), #Mientras que el de arriba nos lleva a la pestaña donde el usuario va a buscar, ésta es la pestaña donde aparecerá lo buscado

]
