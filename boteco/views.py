"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse

from boteco.models import Postagem


def post_postagem(request):
    """Adiciona um post."""
    if request.method == "POST":
        nova = Postagem()
        nova.texto = request.POST["texto"]
        nova.save()

        return HttpResponse("Postagem bem sucedida")
    return HttpResponse("Método não permitido", status=403)
