from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    imagen = models.ImageField(upload_to='perfil_imagenes/', null=True)  
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
