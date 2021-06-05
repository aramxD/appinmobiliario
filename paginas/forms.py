from django import forms
from django.forms import ModelForm
from .models import *


class nuevaPagina(ModelForm):
    class Meta:
        model = Pagina
        fields = '__all__'