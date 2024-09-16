
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

]
