from django.contrib import admin
from .models import *

# Register your models here.


class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'inmueble', 'ciudad',  'colonia', 'vendedor', 'precio') #visualizar columnas


class InmuebleImagenAdmin(admin.ModelAdmin):
    list_display = ('inmueble', 'id') #visualizar columnas




admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(InmuebleImagen, InmuebleImagenAdmin)