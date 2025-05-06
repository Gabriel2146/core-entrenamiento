from rest_framework import viewsets
from .models import PerfilDeportista
from .serializers import PerfilDeportistaSerializer

class PerfilDeportistaViewSet(viewsets.ModelViewSet):
    queryset = PerfilDeportista.objects.all()
    serializer_class = PerfilDeportistaSerializer
