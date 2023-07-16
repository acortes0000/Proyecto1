"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from categorias.views import ListadoCategorias

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('saludo/', saludo),
    # path('segunda_vista/', segunda_vista),
    # path('minombreEs/<nombre>', minombreEs),
    # path('probandoTemplate/', probandoTemplate)
    # Dashboard Categorias
    path('categorias', ListadoCategorias.as_view(template_name = "categorias/index.html"), name='listadodecategorias'),
]
