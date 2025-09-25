from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #se registra el usuario y lo guarda en la BD 
                user=User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()    
                return HttpResponse('Usuario creado') 
            except:    
                return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })                   
        return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden'
                })   

def productos(request):
    return render (request, 'productos.html')