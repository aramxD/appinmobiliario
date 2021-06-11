from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from paginas.models import *
from equipo.models import *
from django.contrib.auth.decorators import login_required


def get_asesor(request):
    user_asesor = Asesor.objects.filter(user=request.user)
    
    if user_asesor.exists():
        return user_asesor.first()
    return None




def home(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    inmueble = Inmueble.objects.filter(featured=True)
    casas = inmueble.filter(inmueble="Casa").order_by('id')
    departamentos = inmueble.filter(inmueble="Departamento").order_by('id')
    comercios = inmueble.filter(inmueble="Comercio").order_by('id')
    terrenos = inmueble.filter(inmueble="Terreno").order_by('id')

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
        
        inmuebles = Inmueble.objects.filter(inmueble=tipo_inmueble).order_by('id')
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
        fotos_detalles = queryfotos.filter(inmueble=detalles).order_by('id')


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
@login_required
def agregar_inmueble(request, tipo_inmueble):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    if request.method == 'POST':
        asesor = get_asesor(request)
        alta_casa = InmuebleForms(request.POST, request.FILES)
        if alta_casa.is_valid():
            casa = alta_casa.save(commit=False)
            casa.vendedor = asesor
            casa.inmueble = tipo_inmueble
            casa.save()
            
            return redirect("listado_asesor", tipo_inmueble)
            
    else:

        context = {
            'pagina_publicada':pagina_publicada,
            'form':InmuebleForms(),
            }
        return render (request, 'agregar_inmueble.html', context)


#USER ONLY
@login_required
def editar_inmueble(request, inmueble_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    queryfotos = InmuebleImagen.objects.all()
    fotos_detalles = queryfotos.filter(inmueble=inmueble_detalles)
    tipo_inmueble = inmueble_detalles.inmueble
    
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
            
            return redirect("listado_asesor", tipo_inmueble)
        except ValueError:
            context = {
                'pagina_publicada':pagina_publicada,
                'fotos_detalles':fotos_detalles,
                'inmueble' : inmueble_detalles,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...',
                
                
            }
            return render(request, 'editar_inmueble.html', context)


#USER ONLY
@login_required
def eliminar_inmueble(request, inmueble_id):
    inmueble_detalles = get_object_or_404(Inmueble, pk=inmueble_id)
    tipo_inmueble = inmueble_detalles.inmueble
    if request.method == 'POST':
        inmueble_detalles.delete()
        return redirect("listado_asesor", tipo_inmueble) 


#FOTOS EXTRAS
@login_required
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


@login_required
def editar_fotos(request, foto_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    foto_detalle = get_object_or_404(InmuebleImagen, pk=foto_id)
    
    inmueble_id = foto_detalle.inmueble.id
    if request.method == 'GET':
        form = FotosInmuebleForms(instance = foto_detalle)
        
        context = {
            'pagina_publicada':pagina_publicada,
            'foto_detalle':foto_detalle,
            'form' : form,
        } 
        return render(request, 'editar_foto.html', context)
    else:
        try:
            form = FotosInmuebleForms(request.POST, request.FILES, instance=foto_detalle)
            form.save()
            
            return redirect('editar_inmueble', inmueble_id)
        except ValueError:
            context = {
                'pagina_publicada':pagina_publicada,
                'fotos_detalles':foto_detalle,
                
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...',
                
                
            }
            return render(request, 'editar_foto.html', context)


#USER ONLY
@login_required
def eliminar_foto(request, foto_id):
    foto_inmueble = get_object_or_404(InmuebleImagen, pk=foto_id)
    inmueble_id = foto_inmueble.inmueble.id
    if request.method == 'POST':
        foto_inmueble.delete()
        return redirect("editar_inmueble", inmueble_id) 


#DASHBOARD
@login_required
def dashboard(request):
    citas = Citas.objects.all()
    paginas = Pagina.objects.all()
    pagina_publicada = paginas.filter(publicar=True)
    asesor = get_asesor(request)
    asesor_is_admin = asesor.is_admin
    if asesor_is_admin:
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
    else:
        inmueble = Inmueble.objects.filter(vendedor=asesor)
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


@login_required
def listado_asesor(request, tipo_inmueble):
    paginas = Pagina.objects.all()
    pagina_publicada = paginas.filter(publicar=True)
    asesor = get_asesor(request)
    asesor_is_admin = asesor.is_admin
    if request.method == 'GET':
        if asesor_is_admin:
            inmuebles = Inmueble.objects.filter(inmueble=tipo_inmueble).order_by('id')
            context = {
            'paginas':paginas,
            'tipo_inmueble':tipo_inmueble,
            'pagina_publicada':pagina_publicada,
            'inmuebles':inmuebles,
            }
            return render (request, 'listado_cartera.html', context)
        else:
            inmuebles = Inmueble.objects.filter(inmueble=tipo_inmueble).filter(vendedor=asesor).order_by('id')
            context = {
            'paginas':paginas,
            'tipo_inmueble':tipo_inmueble,
            'pagina_publicada':pagina_publicada,
            'inmuebles':inmuebles,
            }
            return render (request, 'listado_cartera.html', context)
    else:
        return redirect("dashboard")



@login_required
def listado_citas(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    asesor = get_asesor(request)
    asesor_is_admin = asesor.is_admin
    print(asesor_is_admin)
    if asesor_is_admin:
        citas = Citas.objects.order_by('id')
        context = {
            'citas':citas,
            'pagina_publicada':pagina_publicada,
            }
        return render (request, 'listado_citas.html', context)
    else:
        citas = Citas.objects.filter(asesor=asesor).order_by('id')
        context = {
            'citas':citas,
            'pagina_publicada':pagina_publicada,
            }
        return render (request, 'listado_citas.html', context)



@login_required
def checked_citas(request, cita_id):
    cita = get_object_or_404(Citas, pk=cita_id)
    if request.method == 'POST':
        if cita.checked == False:
            cita.checked = True
            cita.save()
            return redirect("listado_citas")
        else:
            cita.checked = False
            cita.save()
            return redirect("listado_citas")


@login_required
def eliminar_citas(request, cita_id):
    cita = get_object_or_404(Citas, pk=cita_id)
    if request.method == 'POST':
        cita.delete()
        return redirect("listado_citas")