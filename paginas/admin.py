from django.contrib import admin
from .models import *
# Register your models here.


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'creado') #visualizar columnas

admin.site.register(Pagina, PaginaAdmin)