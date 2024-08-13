from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfil_images/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pagina_web = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.user.username