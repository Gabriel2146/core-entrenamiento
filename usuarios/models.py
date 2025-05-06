from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from localizacion.models import Ciudad

# Usuario personalizado
class Usuario(AbstractUser):
    numero_documento = models.CharField(max_length=20, unique=True)

    TIPO_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('ENTRENADOR', 'Entrenador'),
        ('DEPORTISTA', 'Deportista'),
        ('INVITADO', 'Invitado'),
    ]
    tipo = models.CharField(max_length=15, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"

# Validación del dato sensible (documento)
def validar_documento_sensible(valor):
    if not valor.isdigit() or len(valor) < 6:
        raise ValidationError("El número de documento debe ser numérico y tener al menos 6 dígitos.")

# Perfil para deportistas (relación con Usuario)
class PerfilDeportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    fecha_nacimiento = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    documento_sensible = models.CharField(max_length=20, validators=[validar_documento_sensible])

    def __str__(self):
        return f"{self.usuario.username} - Perfil"
