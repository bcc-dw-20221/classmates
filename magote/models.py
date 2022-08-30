from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


STATUS_CORNO = (
    ("cm", "Corno Manso"),
    ("cc", "Corno Cururu"),
    ("ca", "Corno Abelha"),
    ("cp", "Corno Prestativo"),
    ("bg", "Buscando a galha"),
    ("ci", "Corno Indeciso"),
)


class Magote(models.Model):
    lider = models.OneToOneField(get_user_model(), primary_key=True)
    membros = models.ManyToManyField(get_user_model())


class Perfil(models.Model):
    user_id = models.OneToOneField(get_user_model(), primary_key=True)

    qtd_chifres = models.IntegerField(default=1)
    status = models.CharField(max_length=2, choices=STATUS_CORNO, default="ci")
    ultimo_chifre = models.DateTimeField(default=timezone.now)

    procurando_mais = models.BooleanField(
        verbose_name="Procurando mais chifres", default=True
    )
    # Outros campos
