from rest_framework import viewsets
from .models import Pais, Provincia, Ciudad
from .serializers import PaisSerializer, ProvinciaSerializer, CiudadSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

    def get_queryset(self):
        pais_id = self.request.query_params.get('pais')
        if pais_id:
            return self.queryset.filter(pais_id=pais_id)
        return self.queryset

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

    def get_queryset(self):
        provincia_id = self.request.query_params.get('provincia')
        if provincia_id:
            return self.queryset.filter(provincia_id=provincia_id)
        return self.queryset
