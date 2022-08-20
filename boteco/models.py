"""ORM do Blog."""
from django.db import models

# Create your models here.
class Postagem(models.Model):
    """Post de um corno no blog."""

    texto = models.CharField(max_length=140)
