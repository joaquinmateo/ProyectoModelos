"""
URL configuration for modelos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#debo importame las funciones de views
from app_coder.views import crea_curso, lista_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-coder/', include('app_coder.urls')),
]
#Al estar copiado dentro de la carpeta de app_coder, no hace falta tenerlos
#Si la URL consultada es en app-coder, irá al archivo de app_coder.urls y podremos visualizar todas las funciones