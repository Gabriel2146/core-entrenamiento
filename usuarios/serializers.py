from rest_framework import serializers
from .models import PerfilDeportista, Usuario
from localizacion.models import Ciudad

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id', 'nombre']

class PerfilDeportistaSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(read_only=True)
    ciudad_id = serializers.PrimaryKeyRelatedField(
        queryset=Ciudad.objects.all(), source='ciudad', write_only=True
    )

    class Meta:
        model = PerfilDeportista
        fields = [
            'id', 'usuario', 'fecha_nacimiento', 'peso', 'altura',
            'documento_sensible', 'ciudad', 'ciudad_id'
        ]
