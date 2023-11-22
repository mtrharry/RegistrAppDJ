# En views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario
from .serializers import usuarioSerializer, AsignaturaSerializer,AsistenciaSerializer
from rest_framework import generics

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
    # Lógica para procesar el escaneo de QR y confirmar asistencia
    # Aquí deberás extraer la información del QR, asociarla con el estudiante y guardar la asistencia en la base de datos
    # ...

    # Ejemplo de cómo podrías usar el modelo Asistencia
    serializer = AsistenciaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)