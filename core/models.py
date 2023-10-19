from django.db import models

# Create your models here.


class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name = "Id de Usuario")
    nombreUsuario = models.CharField(max_length=50, verbose_name = "Nombre de usuario")
    Contraseña = models.CharField(max_length=50, verbose_name = "Contraseña de usuario")
    Categoria = models.CharField(max_length=50, verbose_name = "Nombre de Categoria")
    Email = models.CharField(max_length=50, verbose_name = "Email de usuario")

    def __str__(self):
        return self.nombreUsuario

