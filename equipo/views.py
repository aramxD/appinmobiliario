from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from inmuebles.views import *
from .models import *
from .forms import *
from paginas.models import *
from django.contrib.auth.decorators import login_required
#from django.shortcuts import HttpResponseRedirect

# Create your views here.


#USER ONLY
@login_required
def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try: 
                user = User.objects.create_user(
                    request.POST['username'], 
                    first_name=request.POST['first_name'], 
                    last_name=request.POST['last_name'], 
                    email=request.POST['email'] , 
                    password=request.POST['password1'])
                
                perfil = Asesor.objects.create(
                    user = User.objects.all().last(),
                    apodo = request.POST['username'], 
                    nombre =request.POST['first_name'], 
                    apeido =request.POST['last_name'], 
                    email =request.POST['email'] , 
                    telefono = request.POST['telefono'] , 
                    foto=request.FILES['img'])
                user.is_staff=True
                user.save()
                perfil.save()
                
                return redirect('home')
            except IntegrityError:
                error = 'Tu nombre de usuario fue tomado, intenta con otro'
                context = {
                    'error':error,
                    'form': form,
                }
                return render(request, 'registro.html', context)
        else:
            error = 'Error al escribir tu contrasena'
            context={'error':error,
                    'form': form,}
            return render(request, 'registro.html', context)
    else:
        context={
            'form': form
        }
        return render(request, 'registro.html', context)


#USER ONLY
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect("home")


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['Password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm() , 'error': 'User or password did not match'})
        else:
            login(request, user)
            return redirect('dashboard')
    else:
        return render(request, 'login.html',  {'form': AuthenticationForm()})


@login_required
def editar_asesor(request, user_id):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    user = get_object_or_404(User, pk=user_id)
    user_asesor = get_object_or_404(Asesor, user=user)
    print(user_asesor)

    form = PerfilForm(instance = user_asesor)
    if request.method == 'POST':
        try: 
            form = PerfilForm(request.POST, request.FILES, instance=user_asesor)
            form.save()
            
            return redirect('home')
        except IntegrityError:
            error = 'Reviza los datos, detecto un error'
            context = {
                'pagina_publicada':pagina_publicada,
                'error':error,
                'form': form,
            }
            return render(request, 'registro.html', context)

    else:
        form = PerfilForm(instance = user_asesor)
        context={
            'pagina_publicada':pagina_publicada,
            'form': form
        }
        return render(request, 'editar_asesor.html', context)


@login_required
def eliminar_asesor(request, user_id):
    
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect("listado_user")
    


@login_required
def listado_user(request):
    pagina_publicada = Pagina.objects.filter(publicar=True)
    asesores = Asesor.objects.order_by("id")


    context = {
        'pagina_publicada': pagina_publicada,
        'asesores':asesores,
    }
    return render (request, 'listado_equipo.html', context)