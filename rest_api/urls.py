from django.urls import path
from rest_api.views import lista_usuario

urlpatterns=[
    path('lista_usuario', lista_usuario, name="Lista Usuario"),
]