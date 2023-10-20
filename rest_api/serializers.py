from rest_framework import serializers
from core.models import Usuario

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario','nombreUsuario', 'Contraseña','Categoria','Email']