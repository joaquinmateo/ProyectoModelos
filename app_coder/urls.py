
from django.urls import path
#debo importame las funciones de views
from .views import *
#Esta es para el logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('crea-curso', crea_curso),
    path('lista-cursos-old/', lista_cursos),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name = "Cursos"),
    path('profesores/', profesores, name = "Profesores"),
    path('estudiantes/', estudiantes, name = "Estudiantes"),
    path('entregables/', entregables, name = "Entregables"),
    path('curso-formulario/', curso_formulario, name = "CursoFormulario"), #Creamos el template
    path('busqueda-camada/', busqueda_camada, name = "BusquedaCamada"), #Creamos el template
    path('buscar-camada/', buscar_camada, name = "BuscarCamada"), #Mientras que el de arriba nos lleva a la pestaña donde el usuario va a buscar, ésta es la pestaña donde aparecerá lo buscado
    path('lista-profesores/', lista_profesores, name = "ListaProfesores"),
    path('crea-profesores/', crea_profesores, name = "CreaProfesores"),
    path('elimina-profesor/<int:id>', eliminar_profesor, name = "EliminaProfesor"),
    path('editar-profesor/<int:id>', editar_profesor, name = "EditarProfesor"),
    path('lista-cursos/', CursoList.as_view(), name = "ListaCursos"),
    path('detalle-curso/<pk>', CursoDetail.as_view(), name = "DetalleCurso"), #Al no definir id como parametro en la class, se pone pk
    path('crea-curso/', CursoCreate.as_view(), name = "CreaCurso"),
    path('actualiza-curso/<pk>', CursoUpdate.as_view(), name = "ActualizaCurso"), 
    path('elimina-curso/<pk>', CursoDelete.as_view(), name = "EliminaCurso"),
    path('login/', login_view, name = "Login"),
    path('registrar/', register, name = "Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "Logout"),
]
