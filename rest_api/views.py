from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario
from .serializers import usuarioSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def lista_usuario(request):
    usuario = Usuario.objects.all()
    serializer = usuarioSerializer(usuario, many=True)
    return Response(serializer.data)