from django.contrib import admin
from .models import Usuario,Categoria,Asignatura,Asistencia
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Asignatura)
admin.site.register(Asistencia)