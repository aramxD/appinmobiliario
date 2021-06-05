from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from paginas.models import *


# Create your views here.
def home(request):
    paginas = Pagina.objects.all()
    inmueble = Inmueble.objects.filter(featured=True)
    casas = inmueble.filter(inmueble="Casa")
    departamentos = inmueble.filter(inmueble="Departamento")
    comercios = inmueble.filter(inmueble="Comercio")
    terrenos = inmueble.filter(inmueble="Terreno")

    context = {
        'paginas':paginas,
        'casas':casas,
        'departamentos':departamentos,
        'comercios':comercios,
        'terrenos':terrenos,
    }
    return render(request, 'home.html', context )


def listado(request, tipo_inmueble):
    paginas = Pagina.objects.all()
    if request.method == 'GET':
        
        inmuebles = Inmueble.objects.filter(inmueble=tipo_inmueble)
        context = {
        'paginas':paginas,
        'inmuebles':inmuebles,
        
        }
        return render (request, 'listado_inmuebles.html', context)
    else:
        pass


def detalles_inmuebles(request, tipo_inmueble, inmueble_id):
    paginas = Pagina.objects.all()
    detalles = get_object_or_404(Inmueble,  pk=inmueble_id)
    
    if detalles.inmueble == tipo_inmueble:
        queryfotos = InmuebleImagen.objects.all()
        fotos_detalles = queryfotos.filter(inmueble=detalles)


        if request.method == 'POST':
            agendar_cita = CitasForms(request.POST)
            if agendar_cita.is_valid():
                asesor = agendar_cita.save(commit=False)
                asesor.asesor = request.POST.get('vendedor', detalles.vendedor)
                asesor.save()
                nota = 'Nos comunicaremos pronto contigo'
                nueva_cita = CitasForms()
                context = {
                    'paginas':paginas,
                    'nota':nota,
                    'nueva_cita':nueva_cita,
                    'detalles' : detalles,
                    'fotos_detalles' : fotos_detalles,
                    }
                return render (request, 'detalles_inmuebles.html', context)
            else:
                nota = 'Favor de revizar que los datos sean correctos'
            nueva_cita = CitasForms()
            context = {
                    'paginas':paginas,
                    'nota':nota,
                    'nueva_cita':nueva_cita,
                    'detalles' : detalles,
                    'fotos_detalles' : fotos_detalles,
                    }
            return render (request, 'detalles_inmuebles.html', context)
        else:
            nota = ''
            nueva_cita = CitasForms()
            context = {
                    'paginas':paginas,
                    'nota':nota,
                    'nueva_cita':nueva_cita,
                    'detalles' : detalles,
                    'fotos_detalles' : fotos_detalles,
                    }
            return render (request, 'detalles_inmuebles.html', context)
    else:
        return redirect("home")


#USER ONLY
def agregar_inmueble(request, tipo_inmueble):
    paginas = Pagina.objects.all()
    if request.method == 'POST':
        alta_casa = InmuebleForms(request.POST, request.FILES)
        if alta_casa.is_valid():
            casa = alta_casa.save(commit=False)
            casa.inmueble = tipo_inmueble
            casa.save()
            
            return redirect("home")
            
    else:

        context = {
            'paginas':paginas,
            'form':InmuebleForms(),
            }
        return render (request, 'agregar_inmueble.html', context)


#USER ONLY
def editar_inmueble(request, inmueble_id):
    paginas = Pagina.objects.all()
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    queryfotos = InmuebleImagen.objects.all()
    fotos_detalles = queryfotos.filter(inmueble=inmueble_detalles)
    
    if request.method == 'GET':
        form = InmuebleForms(instance = inmueble_detalles)
        context = {
            'paginas':paginas,
            'fotos_detalles':fotos_detalles,
            'inmueble' : inmueble_detalles,
            'form' : form,
            
        } 
        return render(request, 'editar_inmueble.html', context)
    else:
        try:
            form = InmuebleForms(request.POST, request.FILES, instance=inmueble_detalles)
            form.save()
            return redirect("home")
            
        except ValueError:
            context = {
                'paginas':paginas,
                'fotos_detalles':fotos_detalles,
                'inmueble' : inmueble_detalles,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...',
                
            }
            return render(request, 'editar_inmueble.html', context)


#USER ONLY
def eliminar_inmueble(request, inmueble_id):
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    if request.method == 'POST':
        inmueble_detalles.delete()
        return redirect('home') 



def listado_inmuebles(request):
    paginas = Pagina.objects.all()
    inmueble = Inmueble.objects.all()
    casas = inmueble.filter(inmueble="Casa")
    departamentos = inmueble.filter(inmueble="Departamento")
    comercios = inmueble.filter(inmueble="Comercio")
    terrenos = inmueble.filter(inmueble="Terreno")
    
    context = {
        'paginas':paginas,
        'casas' : casas,
        'departamentos' : departamentos,
        'comercios' : comercios,
        'terrenos' : terrenos,
    }
    return render(request, 'listado_cartera.html', context)
