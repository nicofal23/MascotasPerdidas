from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Perfil
        fields = ['telefono', 'imagen']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_username(self):
        username = self.cleaned_data['username']
        if self.user:
            if User.objects.filter(username__iexact=username).exclude(pk=self.user.pk).exists():
                raise forms.ValidationError("El nombre de usuario ya está en uso.")
        else:
            if User.objects.filter(username__iexact=username).exists():
                raise forms.ValidationError("El nombre de usuario ya está en uso.")
        return username

    def save(self, commit=True):
        perfil = super(PerfilForm, self).save(commit=False)
        if self.user:
            user = self.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                perfil.save()
        return perfil


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
