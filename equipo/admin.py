from django.contrib import admin
from .models import *
# Register your models here.


class AsesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre') #visualizar columnas

class CitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'telefono', 'asesor','whattsapp') #visualizar columnas

admin.site.register(Asesor, AsesorAdmin)
admin.site.register(Citas, CitasAdmin)