from django.contrib import admin
from .models import Curso, Entregable, Estudiantes, Profesor

# Register your models here.
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiantes)
admin.site.register(Profesor)


#Ahora veremos como en el dministrador se agregaron los modelos, con su base de datos también modificable

#Para que figuren como string vamos a modificar los modelos de models.py agregando el def __str__(), de ésta manera figura en el administrador con el nombre particular


