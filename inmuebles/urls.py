from django.contrib import admin
from django.urls import  path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('listado/<str:tipo_inmueble>', listado, name='listado'),

    # CASAS
    
    path('casa-detalle/<casa_id>', casa_detalles, name='casa_detalles'),
    path('casa-agregar/', casa_agregar, name='casa_agregar'),
    path('casa-editar/<casa_id>', casa_editar, name='casa_editar'),
    path('casa-eliminar/<casa_id>', casa_eliminar, name='casa_eliminar')
]   