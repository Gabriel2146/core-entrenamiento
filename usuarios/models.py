from localizacion.models import Ciudad
from django.core.exceptions import ValidationError

def validar_documento_sensible(valor):
    if not valor.isdigit() or len(valor) < 6:
        raise ValidationError("El número de documento debe ser numérico y tener al menos 6 dígitos.")

class PerfilDeportista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    fecha_nacimiento = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    documento_sensible = models.CharField(max_length=20, validators=[validar_documento_sensible])

    def __str__(self):
        return f"{self.usuario.username} - Perfil"
