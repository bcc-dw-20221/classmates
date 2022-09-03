"""ORM do Blog."""
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class Postagem(models.Model):
    """Post de um corno no blog."""

    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=None,
        related_name="postagens",
    )

    texto = models.CharField(max_length=140)

    timestamp = models.DateTimeField(default=timezone.now)

    curtidas = models.ManyToManyField(
        get_user_model(), related_name="curtidas_postagem", blank=True
    )

    def __str__(self) -> str:
        return f"{self.autor} postou: {self.texto}"


class Comentario(models.Model):
    autor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )  # Many to one

    postagem = models.ForeignKey(
        Postagem, on_delete=models.CASCADE, default=None
    )

    texto = models.CharField(max_length=140)
    timestamp = models.DateTimeField(default=timezone.now)

    curtidas = models.ManyToManyField(
        get_user_model(), related_name="curtidas_comentarios", blank=True
    )

    def __str__(self) -> str:
        return f"Comentário de {self.autor}"


class TipoDeCorno(models.Model):
    nome = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self) -> str:
        return self.nome


class Magote(models.Model):
    lider = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="magote_lider",
    )
    membros = models.ManyToManyField(
        get_user_model(), related_name="magote_membros"
    )

    def __str__(self) -> str:
        return f"Magote liderado por {self.lider.username}"  # pylint: disable=E1101


class Bebida(models.Model):
    nome = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self) -> str:
        return self.nome


def user_directory_path(instance, filename):
    """Trouxe direto da documentação, para simplificar."""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    extension = filename.split(".")[-1]
    return f"user_{instance.user.id}/profile_pic.{extension}"


class Perfil(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="perfil",
    )

    foto_perfil = models.ImageField(
        "Foto de perfil",
        blank=True,
        upload_to=user_directory_path,
        default="user_default/profile.jpg",
    )

    qtd_chifres = models.IntegerField(default=1)
    status = models.ForeignKey(
        TipoDeCorno, null=True, on_delete=models.SET_DEFAULT, default=None
    )
    ultimo_chifre = models.DateTimeField(default=timezone.now)

    bebida_preferida = models.ForeignKey(
        Bebida, null=True, on_delete=models.SET_NULL
    )

    procurando_mais = models.BooleanField(
        verbose_name="Procurando mais chifres", default=True
    )

    def __str__(self) -> str:
        return f"Perfil de {self.user.username}"  # pylint: disable=E1101
