from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def home(request):
    inmueble = Inmueble.objects.all()
    casas = inmueble.filter(inmueble="Casa")
    departamentos = inmueble.filter(inmueble="Departamento")
    comercios = inmueble.filter(inmueble="Comercio")
    terrenos = inmueble.filter(inmueble="Terreno")

    context = {
        'casas':casas,
        'departamentos':departamentos,
        'comercios':comercios,
        'terrenos':terrenos,
    }
    return render(request, 'home.html', context )


def listado(request, tipo_inmueble):
    if request.method == 'GET':
        
        inmuebles = Inmueble.objects.filter(inmueble=tipo_inmueble)
        context = {
        'inmuebles':inmuebles,
        
        }
        return render (request, 'listado_inmuebles.html', context)
    else:
        pass


def casa_detalles(request, casa_id):
    detalles = get_object_or_404(Inmueble, pk=casa_id)
    if detalles.inmueble == "Casa":
        queryfotos = InmuebleImagen.objects.all()
        fotos_detalles = queryfotos.filter(casa=detalles)
        context = {
            
            'detalles' : detalles,
            'fotos_detalles' : fotos_detalles,
            }
        return render (request, 'casa_detalles.html', context)
    else:
        return redirect("home")


def casa_agregar(request):
    if request.method == 'POST':
        alta_casa = InmuebleForms(request.POST, request.FILES)
        if alta_casa.is_valid():
            casa = alta_casa.save()
            return redirect("home")
            
    else:

        context = {
            'form':InmuebleForms(),
            }
        return render (request, 'casa_agregar.html', context)


def casa_editar(request, casa_id):
    inmueble_detalles = get_object_or_404(Inmueble, pk=casa_id)
    queryfotos = InmuebleImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=inmueble_detalles)
    
    if request.method == 'GET':
        form = InmuebleForms(instance = inmueble_detalles)
        context = {
            'fotos_detalles':fotos_detalles,
            'inmueble' : inmueble_detalles,
            'form' : form,
            
        } 
        return render(request, 'casa_editar.html', context)
    else:
        try:
            form = InmuebleForms(request.POST, request.FILES, instance=inmueble_detalles)
            form.save()
            return redirect("home")
            
        except ValueError:
            context = {
                'fotos_detalles':fotos_detalles,
                'inmueble' : inmueble_detalles,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...',
                
            }
            return render(request, 'editar_casa.html', context)



def casa_eliminar(request, casa_id):
    inmueble_detalles = get_object_or_404(Inmueble, pk=casa_id)
    if request.method == 'POST':
        inmueble_detalles.delete()
        return redirect('home') 
    