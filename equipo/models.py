from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Asesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=20)
    apeido = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    foto = models.ImageField(verbose_name="perfil", upload_to="images/user", blank=True)

    def __str__(self):
        user = self.nombre + " " + self.apeido
        return user


class Citas(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    whattsapp = models.BooleanField(default=False)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre_completo