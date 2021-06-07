from django.db import models
from ckeditor.fields import RichTextField
from equipo.models import Asesor

# Create your models here.
TIPO_INMUEBLE = (
    ('Departamento', 'Departamento'),
    ('Casa', 'Casa'),
    ('Terreno', 'Terreno'),
    ('Comercio', 'Comercio'),
    )
TIPO_CONTRATO = (
    ('Venta', 'Venta'),
    ('Renta', 'Renta'),)



class Inmueble(models.Model):
    #Datos generales
    inmueble = models.CharField(choices=TIPO_INMUEBLE, default='Casa', max_length=15)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=2500000)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/landing", blank=True)


    #Datos particulares
    
    m2_construccion = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    m2_terreno = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    num_habitaciones = models.IntegerField(default=0, verbose_name="Numero de cuartos", null=True, blank=True)
    num_banos = models.DecimalField(max_digits=2, decimal_places=1, default=1, verbose_name="Numero de baños", null=True, blank=True)
    estacionamiento = models.IntegerField(default=0, verbose_name="Numero de estacionamientos", blank=True)
    nivel =  models.IntegerField( verbose_name="Nivel", null=True,  blank=True)
    amenidades = models.BooleanField(default=False)
    notas = RichTextField(blank=True)
    
    
    #ubicacion
    calle = models.CharField(max_length=40, blank=True)
    numero_ext = models.CharField(max_length=8, blank=True)
    numero_int = models.CharField(max_length=4, blank=True)
    colonia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40, default='Tijuana')
    estado = models.CharField(max_length=40, default='Baja California')
    pais = models.CharField(max_length=40, default='Mexico')
    codigo_postal = models.CharField(max_length=6, blank=True )
    latitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=15, decimal_places=9, verbose_name="longitud", null=True, blank=True)
    featured = models.BooleanField(default=True, verbose_name="Quieres que aparesca en la pagina principal?")
    
    #transaccion
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO, default='Venta', max_length=15)
    termino = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    vendedor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        nombre = self.inmueble + ' en '  + self.colonia
        return nombre


class InmuebleImagen(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/inmuebles")
    alt = models.CharField(max_length=40, blank=True)        