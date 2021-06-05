from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

#USER ONLY
def listado_paginas(request):
    paginas = Pagina.objects.all()
    context= {
        'paginas' : paginas,
    }
    return render(request, 'listado_paginas.html', context)



def pagina(request, slug):
    paginas = Pagina.objects.all()
    pagina = get_object_or_404(Pagina, slug=slug)

    context = {
        'paginas' : paginas,
        'pagina' : pagina,
    }
    return render(request, 'pagina.html', context)


#USER ONLY
def nueva_pagina(request):
    if request.method == 'POST':
        alta_pagina = nuevaPagina(request.POST, request.FILES)
        if alta_pagina.is_valid():
            pagina = alta_pagina.save()
            return redirect("home")
            
    else:

        context = {
            'form':nuevaPagina(),
            }
        return render (request, 'nueva_pagina.html', context)
    
