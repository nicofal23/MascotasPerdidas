from django.shortcuts import render, redirect, get_object_or_404
from .forms import PerfilForm, RegistroForm
from .models import Perfil
from django.contrib.auth import login
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = RegistroForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            perfil = form.save(commit=False)
            
            if 'imagen' in request.FILES:
                print("Imagen cargada:", request.FILES['imagen'].name)
                
                # Eliminar la imagen anterior si es necesario
                if perfil.imagen:
                    perfil.imagen.delete(save=False)
                
                # Asigna la nueva imagen
                perfil.imagen = request.FILES['imagen']
            
            perfil.save()  # Asegúrate de guardar el perfil después de hacer todos los cambios
            
            return redirect('profile')
        else:
            print("Formulario no válido:", form.errors)
    else:
        form = PerfilForm(instance=perfil, user=request.user)

    return render(request, 'accounts/perfil.html', {'form': form})

def ver_perfil(request, user_id):
    perfil = get_object_or_404(Perfil, user_id=user_id)
    publicaciones = Post.objects.filter(autor=perfil.user)

    return render(request, 'accounts/ver_perfil.html', {
        'perfil': perfil,
        'publicaciones': publicaciones,
    })



def logout_confirmation(request):
    return render(request, 'accounts/logout.html')



from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin/manage_users.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')

@user_passes_test(lambda u: u.is_superuser)
def give_admin_privileges(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    return redirect('manage_users')




