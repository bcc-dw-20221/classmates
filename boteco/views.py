"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from boteco.models import Postagem


def get_postagens(request):
    """Retorna todas as postagens."""
    postagens = Postagem.objects.all()

    postagen_json = serializers.serialize("json", postagens)

    resp = {
        "postagens": postagen_json,
    }

    return JsonResponse(resp)


def get_postagem(request, postagem_id):
    """Retorna todas as postagens."""
    postagens = Postagem.objects.get(pk=postagem_id)

    postagem_json = serializers.serialize("json", [postagens])

    resp = {"postagem": postagem_json}

    return JsonResponse(resp)


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
