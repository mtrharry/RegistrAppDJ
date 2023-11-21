from django.urls import path
from rest_api.views import lista_usuario, AsignaturasDocenteView

urlpatterns = [
    path('lista_usuario', lista_usuario, name="Lista Usuario"),
    path('asignaturas_docente/<int:id_docente>/', AsignaturasDocenteView.as_view(), name="Asignaturas Docente"),
]