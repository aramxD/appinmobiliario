from django import forms
from django.forms import ModelForm
from .models import *
from equipo.models import *



class CitasForms(ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'
        #exclude = ('asesor',)
        widgets = {'asesor': forms.HiddenInput()}
        labels = {
            "whattsapp": "Recibir mensaje de Whattsapp?  "
        }


class InmuebleForms(ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Inmueble
        fields = '__all__'
        exclude = ('created',)
        #widgets = {'vendedor': forms.HiddenInput()}
        labels = {
            "precio": "Precio de inmueble (En MXN) ",
            "amenidades": "El inmueble cuenta con amenidades? ",
            "termino": "Ya se vendio el Inmueble?",
            "notas": "Aqui puedes poner una breve descripcion del Inmueble"
        }


class FotosInmuebleForms(ModelForm):
    class Meta:
        model = InmuebleImagen
        fields = '__all__'