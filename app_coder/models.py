from django.db import models

# Create your models here.
class Curso(models.Model):
    #mchar
    nombre = models.CharField(max_length=50)
    #mint
    camada = models.IntegerField()
    #En la terminal escrbir python manage.py showmigrations
    #En settings.py en INSTALLED APPS
    #En la terminal escrbir python manage.py makemigrations
    #Se creó en la carpeta migartions el archivo 0001_.py
    #Ese archivo figura con el showmigrations pero no estará en el DB Browser
    #Para agregarlo escribir en la terminal python manage.py migrate
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'My Courses...'
        ordering = ('nombre', 'camada')

#T ODO LO QUE SIGUE VA EN LA TERMINAL
    #python manage.py shell para abrir una terminal interactiva
    #from app_coder.models import Curso
    #nuevo_curso = Curso(nombre="Python basico", camada = 80123)       (Este nuevo curso todavía no existe en DB Browser - Browse Data - Table: app_coder_curso)
    #nuevo_curso.save()
    #exit() para cerrar terminal

    #Nos vamos a views.py para crear las funciones

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #memail
    email = models.EmailField()
    #curso = models.ManyToManyField(Curso, related_name="estudiante_curso")
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

#Hacemos un python manage.py makemigrations y en la carpeta migrations se creeará el 0002
#python manage.py migrate para llevarlo al DB Browser

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

#Si hacemos modificaciones a clases ya migradas al Db Browser debemos escribirle a la modificación null=True 
# En migrations se creará como un nuevo archivo, pero en Db Browser aparece como un atributo más  

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    #mdat
    fecha_entrega = models.DateField()
    #mbool
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE) #De ésta manera si se elimina un estudiante también lo hará su entregable
    def __str__(self):
        return f'{self.nombre}'
    #Control c para matar el servidor y hacemos un python manage.py makemigrations
    #IMPORTANTE, ahora voy a matar la base de datos y las migraciones (los 000X) para no darle a estudiante el valor null
    #python manage.py migrate
    #Volvemos a crear el superusuario xq se borró
    #Si en el administrador agregamos un entregable nos pedirá elegir a un estudiante, para eso, será necesario tener un estudiante creado
    #Incluso se pueden crear estudiantes desde el mismo Entregables


