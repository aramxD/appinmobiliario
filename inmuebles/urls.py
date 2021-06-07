from django.contrib import admin
from django.urls import  path
from .views import *

urlpatterns = [
    path('', home, name='home'),

    #listado para cada tipo de inmueble :D
    path('listado/<str:tipo_inmueble>', listado, name='listado'),
    path('detalle/<str:tipo_inmueble>/<inmueble_id>', detalles_inmuebles, name='detalles_inmuebles'),
    path('agregar/<str:tipo_inmueble>', agregar_inmueble, name='agregar_inmueble'),
    path('editar/<inmueble_id>', editar_inmueble, name='editar_inmueble'),
    path('eliminar/<inmueble_id>', eliminar_inmueble, name='eliminar_inmueble'),

    #Listado tipo dashboard
    path('listado_inmuebles', listado_inmuebles, name='listado_inmuebles'),
    path('agregar/<inmueble_id>/foto', agregar_fotos, name='agregar_fotos'),

    path('dashboard', dashboard, name='dashboard'),

    

    ]   