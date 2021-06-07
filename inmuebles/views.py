from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from paginas.models import *


# Create your views here.
def home(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    inmueble = Inmueble.objects.filter(featured=True)
    casas = inmueble.filter(inmueble="Casa")
    departamentos = inmueble.filter(inmueble="Departamento")
    comercios = inmueble.filter(inmueble="Comercio")
    terrenos = inmueble.filter(inmueble="Terreno")

    context = {
        'pagina_publicada':pagina_publicada,
        'casas':casas,
        'departamentos':departamentos,
        'comercios':comercios,
        'terrenos':terrenos,
    }
    return render(request, 'home.html', context )


def listado(request, tipo_inmueble):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    if request.method == 'GET':
        
        inmuebles = Inmueble.objects.filter(inmueble=tipo_inmueble)
        context = {
        'pagina_publicada':pagina_publicada,
        'inmuebles':inmuebles,
        
        }
        return render (request, 'listado_inmuebles.html', context)
    else:
        return redirect("home")


def detalles_inmuebles(request, tipo_inmueble, inmueble_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
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
                    'pagina_publicada':pagina_publicada,
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
                    'pagina_publicada':pagina_publicada,
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
                    'pagina_publicada':pagina_publicada,
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
    pagina_publicada = Pagina.objects.filter(publicar=True)
    if request.method == 'POST':
        alta_casa = InmuebleForms(request.POST, request.FILES)
        if alta_casa.is_valid():
            casa = alta_casa.save(commit=False)
            casa.inmueble = tipo_inmueble
            casa.save()
            
            return redirect("home")
            
    else:

        context = {
            'pagina_publicada':pagina_publicada,
            'form':InmuebleForms(),
            }
        return render (request, 'agregar_inmueble.html', context)


#USER ONLY
def editar_inmueble(request, inmueble_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    queryfotos = InmuebleImagen.objects.all()
    fotos_detalles = queryfotos.filter(inmueble=inmueble_detalles)

    
    if request.method == 'GET':
        form = InmuebleForms(instance = inmueble_detalles)
        
        context = {
            'pagina_publicada':pagina_publicada,
            'fotos_detalles':fotos_detalles,
            'inmueble' : inmueble_detalles,
            'form' : form,
            
            
        } 
        return render(request, 'editar_inmueble.html', context)
    else:
        try:
            form = InmuebleForms(request.POST, request.FILES, instance=inmueble_detalles)
            form.save()
            
            return redirect("listado_inmuebles")

        
            
        except ValueError:
            context = {
                'pagina_publicada':pagina_publicada,
                'fotos_detalles':fotos_detalles,
                'inmueble' : inmueble_detalles,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...',
                
                
            }
            return render(request, 'editar_inmueble.html', context)


def agregar_fotos(request, inmueble_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    
    if request.method == 'POST':
        foto_inmueble = FotosInmuebleForms(request.POST, request.FILES)
        print(foto_inmueble)
        if foto_inmueble.is_valid():
            
            foto = foto_inmueble.save(commit=False)
            foto.inmueble = inmueble_detalles
            foto.save()
            return redirect('editar_inmueble', inmueble_id)
        else:
            context = {
            'error':"Error en los datos",
            'pagina_publicada':pagina_publicada,
            'form':FotosInmuebleForms(),
            }
        return render (request, 'agregar_foto.html', context)
    else:
        
        context = {
            'pagina_publicada':pagina_publicada,
            'form':FotosInmuebleForms(),
            }
        return render (request, 'agregar_foto.html', context)

#USER ONLY
def eliminar_inmueble(request, inmueble_id):
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    if request.method == 'POST':
        inmueble_detalles.delete()
        return redirect('home') 



def listado_inmuebles(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    inmueble = Inmueble.objects.all()
    casas = inmueble.filter(inmueble="Casa")
    departamentos = inmueble.filter(inmueble="Departamento")
    comercios = inmueble.filter(inmueble="Comercio")
    terrenos = inmueble.filter(inmueble="Terreno")
    
    context = {
        'pagina_publicada':pagina_publicada,
        'casas' : casas,
        'departamentos' : departamentos,
        'comercios' : comercios,
        'terrenos' : terrenos,
    }
    return render(request, 'listado_cartera.html', context)


def dashboard(request):
    citas = Citas.objects.all()
    paginas = Pagina.objects.all()
    pagina_publicada = paginas.filter(publicar=True)
    
    inmueble = Inmueble.objects.all()
    casas = inmueble.filter(inmueble="Casa")
    departamentos = inmueble.filter(inmueble="Departamento")
    comercios = inmueble.filter(inmueble="Comercio")
    terrenos = inmueble.filter(inmueble="Terreno")
    
    context = {
        'citas':citas,
        'paginas':paginas,
        'pagina_publicada':pagina_publicada,
        'casas' : casas,
        'departamentos' : departamentos,
        'comercios' : comercios,
        'terrenos' : terrenos,
    }
    return render(request, 'dashboard.html', context)