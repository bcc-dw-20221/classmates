"""Models do meuauth."""
from django.db import models
from django.contrib.auth import get_user_model

tipo_corno = (
    ("manso", "Corno manso"),
    ("cururu", "Cururu"),
)

# Create your models here.
class CornoProfile(models.Model):
    """Dados extras do perfil de um corno."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, choices=tipo_corno, default="manso")
