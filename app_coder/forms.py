from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField() #Tenemos que importarlo a views.py

class ProfesorFormulario(forms.Form):
    nombre= forms.CharField()
    apellido = forms.CharField()
    profesion = forms.CharField()
    email = forms.EmailField()