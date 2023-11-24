from rest_framework import serializers
from core.models import Usuario,Asignatura,Asistencia
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ['id', 'nombre', 'sigla', 'seccion']

class usuarioSerializer(serializers.ModelSerializer):
    asignaturas = AsignaturaSerializer(many=True, read_only=True)
    class Meta:
        model = Usuario
        fields = ['idUsuario','nombreUsuario', 'contraseña','categoria','email','asignaturas']

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['usuario', 'asignatura', 'fecha', 'hora']