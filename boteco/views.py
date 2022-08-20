"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse
from django.core import serializers

from boteco.models import Postagem


def get_postagens(request):
    """Retorna todas as postagens."""
    postagens = Postagem.objects.all()

    resp_json = serializers.serialize("json", postagens)

    return HttpResponse(resp_json, content_type="application/json")


def get_postagem(request, postagem_id):
    """Retorna todas as postagens."""
    postagem = Postagem.objects.filter(pk=postagem_id)

    postagem_json = serializers.serialize("json", postagem)

    return HttpResponse(postagem_json, content_type="application/json")


def post_postagem(request):
    """Adiciona um post."""
    if request.method == "POST":
        nova = Postagem()
        nova.texto = request.POST["texto"]
        nova.save()

        return HttpResponse("Postagem bem sucedida")
    return HttpResponse("Método não permitido", status=403)


def delete_postagem(request, postagem_id):
    post = Postagem.objects.get(pk=postagem_id)
    post.delete()

    return HttpResponse("Deletado com sucesso.")
