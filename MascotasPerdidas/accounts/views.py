from django.shortcuts import render, redirect, get_object_or_404
from .forms import PerfilForm, RegistroForm
from .models import Perfil
from django.contrib.auth import login
from blog.models import Post

def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(user=user)
            login(request, user)
            return redirect('profile')
        else:
            print(form.errors)  # Esto imprimirá los errores del formulario en la consola.
    else:
        form = RegistroForm()
    return render(request, 'registration/signup.html', {'form': form})
  # Asegúrate de que Post esté importado desde el módulo correcto


def profile(request):
    if request.user.is_authenticated:
        print(f"Usuario autenticado: {request.user.username}")
    else:
        print("Usuario no autenticado")

    perfil, created = Perfil.objects.get_or_create(user=request.user)
    user_posts = Post.objects.filter(autor=request.user)
    print(f"Publicaciones del usuario: {user_posts}")

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PerfilForm(instance=perfil)
    print(f"Publicaciones del usuario: {list(user_posts)}")
    print(f"Número de publicaciones: {user_posts.count()}")

    return render(request, 'accounts/profile.html', {
        'form': form,
        'user_posts': user_posts
    })


def ver_perfil(request, user_id):
    perfil = get_object_or_404(Perfil, user_id=user_id)
    return render(request, 'accounts/ver_perfil.html', {'perfil': perfil})



def logout_confirmation(request):
    return render(request, 'accounts/logout.html')