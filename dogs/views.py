from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Dog
from .forms import DogForm, UserRegisterForm


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


def dog_detail(request, pk):
    """Vista de detalle de un perro"""
    dog = get_object_or_404(Dog, pk=pk, is_active=True)
    context = {
        'dog': dog
    }
    return render(request, 'dogs/dog_detail.html', context)


@login_required
def dog_create(request):
    """Vista para crear un nuevo perro (solo usuarios autenticados)"""
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.publisher = request.user
            dog.save()
            messages.success(request, '¡Perro publicado exitosamente!')
            return redirect('dogs:my_dogs')
    else:
        form = DogForm()

    context = {
        'form': form,
        'title': 'Publicar Perro en Adopción'
    }
    return render(request, 'dogs/dog_form.html', context)


@login_required
def dog_edit(request, pk):
    """Vista para editar un perro existente"""
    dog = get_object_or_404(Dog, pk=pk, publisher=request.user)

    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perro actualizado exitosamente!')
            return redirect('dogs:my_dogs')
    else:
        form = DogForm(instance=dog)

    context = {
        'form': form,
        'dog': dog,
        'title': 'Editar Perro'
    }
    return render(request, 'dogs/dog_form.html', context)


@login_required
def my_dogs(request):
    """Vista para ver los perros publicados por el usuario"""
    dogs = Dog.objects.filter(publisher=request.user).order_by('-created_at')
    context = {
        'dogs': dogs
    }
    return render(request, 'dogs/my_dogs.html', context)


def register(request):
    """Vista de registro de usuarios"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def user_login(request):
    """Vista de login"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'registration/login.html')


def user_logout(request):
    """Vista de logout"""
    logout(request)
    messages.success(request, '¡Sesión cerrada exitosamente!')
    return redirect('home')
