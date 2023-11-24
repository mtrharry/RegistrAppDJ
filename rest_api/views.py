# En views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario
from .serializers import usuarioSerializer, AsignaturaSerializer,AsistenciaSerializer
from rest_framework import generics
from datetime import datetime

@csrf_exempt
@api_view(['GET'])
def lista_usuario(request):
    usuarios = Usuario.objects.all()
    serializer = usuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

class AsignaturasDocenteView(generics.ListAPIView):
    serializer_class = AsignaturaSerializer

    def get_queryset(self):
        # Obtener el ID del docente desde la URL
        id_docente = self.kwargs['id_docente']
        # Obtener las asignaturas asociadas a ese docente
        asignaturas = Usuario.objects.get(idUsuario=id_docente).asignaturas.all()
        return asignaturas
    
@api_view(['POST'])
def escanear_qr(request):
    # Imprimir los datos recibidos
    print("Datos recibidos:", request.data)

    # Obtener la fecha en el formato correcto
    fecha_str = request.data.get('fecha', '')
    fecha_obj = datetime.strptime(fecha_str, '%d-%m-%Y').date()

    # Actualizar la fecha en los datos antes de pasar al serializador
    request.data['fecha'] = fecha_obj

    # Ejemplo de cómo podrías usar el modelo Asistencia
    serializer = AsistenciaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)