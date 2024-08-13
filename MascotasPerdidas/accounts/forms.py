from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen', 'descripcion', 'pagina_web', 'telefono']


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=15, required=True)  # Agregar campo de teléfono

    class Meta:
        model = User
        fields = ["username", "email", "telefono", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            perfil = Perfil(user=user, telefono=self.cleaned_data["telefono"])
            perfil.save()
        return user
