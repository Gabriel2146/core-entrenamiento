from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    numero_documento = models.CharField(max_length=20, unique=True)
    TIPO_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('ENTRENADOR', 'Entrenador'),
        ('DEPORTISTA', 'Deportista'),
        ('INVITADO', 'Invitado'),
    ]
    tipo = models.CharField(max_length=15, choices=TIPO_USUARIO)
