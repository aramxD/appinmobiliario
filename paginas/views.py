from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

#USER ONLY
@login_required
def listado_paginas(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    paginas = Pagina.objects.all()
    context= {
        'pagina_publicada':pagina_publicada,
        'paginas' : paginas,
    }
    return render(request, 'listado_paginas.html', context)



def pagina(request, slug):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    pagina = get_object_or_404(Pagina, slug=slug)

    context = {
        'pagina_publicada' : pagina_publicada,
        'pagina' : pagina,
    }
    return render(request, 'pagina.html', context)


#USER ONLY
@login_required
def nueva_pagina(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    if request.method == 'POST':
        alta_pagina = nuevaPagina(request.POST, request.FILES)
        if alta_pagina.is_valid():
            pagina = alta_pagina.save()
            return redirect("home")
            
    else:

        context = {
            'pagina_publicada':pagina_publicada,
            'form':nuevaPagina(),
            }
        return render (request, 'nueva_pagina.html', context)
    

@login_required
def editar_pagina(request, pagina_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    pagina = get_object_or_404(Pagina, pk=pagina_id)

    if request.method =='GET':
        form = nuevaPagina(instance= pagina)
        context={
            'form':form,
            'pagina_publicada':pagina_publicada,
        }
        return render(request, 'editar_pagina.html', context)
    else: 
        try:
            form = nuevaPagina(request.POST, request.FILES, instance=pagina)
            form.save()
            return redirect("listado_paginas")
        except ValueError:
            context={
            'form':form,
            'pagina_publicada':pagina_publicada,
            'nota':'Error en los datos',
        }
        return render(request, 'editar_pagina.html', context)



@login_required
def eliminar_pagina(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    if request.method == 'POST':
        pagina.delete()
        return redirect("listado_paginas")