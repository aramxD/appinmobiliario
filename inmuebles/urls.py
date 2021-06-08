from django.contrib import admin
from django.urls import  path
from .views import *

urlpatterns = [
    #PUBLICO
    path('', home, name='home'),

    #PUBLICO listado para cada tipo de inmueble :D
    path('listado/<str:tipo_inmueble>', listado, name='listado'),
    path('detalle/<str:tipo_inmueble>/<inmueble_id>', detalles_inmuebles, name='detalles_inmuebles'),

    #USER
    path('agregar/<str:tipo_inmueble>', agregar_inmueble, name='agregar_inmueble'),
    path('editar/<inmueble_id>', editar_inmueble, name='editar_inmueble'),
    path('eliminar/<inmueble_id>', eliminar_inmueble, name='eliminar_inmueble'),

    #Listado tipo dashboard

    #USER
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/<str:tipo_inmueble>', listado_asesor, name='listado_asesor'),
    
    #USER Fotos extras
    path('agregar/<inmueble_id>/foto', agregar_fotos, name='agregar_fotos'),
    path('editar-foto/<foto_id>', editar_fotos, name='editar_fotos'),
    path('eliminar-foto/<foto_id>', eliminar_foto, name='eliminar_foto'),

    ]   