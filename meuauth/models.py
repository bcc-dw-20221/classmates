from django.db import models
from django.contrib.auth.models import User

tipo_corno = (
    ("manso", "Corno manso"),
    ("cururu", "Cururu"),
)

# Create your models here.
class CornoProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, choices=tipo_corno, default="manso")
