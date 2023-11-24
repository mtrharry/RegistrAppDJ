from django.db import models

# Create your models here.

    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Categoría")

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de Asignatura")
    sigla = models.CharField(max_length=10, verbose_name="Sigla de Asignatura")
    seccion = models.CharField(max_length=10, verbose_name="Sección de Asignatura")

    def __str__(self):
        return f"{self.nombre} - {self.sigla} - {self.seccion}"
        
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name="Id de Usuario")
    nombreUsuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    contraseña = models.CharField(max_length=50, verbose_name="Contraseña de usuario")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría del usuario")
    email = models.EmailField(max_length=50, verbose_name="Email de usuario")
    asignaturas = models.ManyToManyField(Asignatura, blank=True, related_name="usuarios", verbose_name="Asignaturas asociadas")

    def __str__(self):
        return self.nombreUsuario

class Asistencia(models.Model):
    
    usuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    asignatura = models.CharField(max_length=50, verbose_name="Asignatura")
    fecha = models.DateField(verbose_name="Fecha de la asistencia")
    hora = models.TimeField(verbose_name="Hora de registro")

    def __str__(self):
        return f"{self.usuario} - {self.asignatura} - {self.fecha} - {self.hora}"