from django.shortcuts import render
from .models import Dog


def home(request):
    """Vista de la página principal"""
    dogs = Dog.objects.filter(is_active=True, status='disponible').order_by('-created_at')[:6]
    context = {
        'dogs': dogs
    }
    return render(request, 'home.html', context)


def dog_list(request):
    """Vista de lista de perros"""
    dogs = Dog.objects.filter(is_active=True, status='disponible').order_by('-created_at')
    context = {
        'dogs': dogs
    }
    return render(request, 'dogs/dog_list.html', context)
