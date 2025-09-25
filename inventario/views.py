from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registrarse(request):
    return render(request, 'registrarse.html',{
        'form': UserCreationForm
    })
