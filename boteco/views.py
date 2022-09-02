"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse
from django.core import serializers

from django.contrib.auth import get_user_model

from django.views.decorators.http import require_http_methods

from boteco.models import Postagem


@require_http_methods(["GET"])
def get_postagens(request):
    """Retorna todas as postagens."""
    postagens = Postagem.objects.all()

    resp_json = serializers.serialize("json", postagens)

    return HttpResponse(resp_json, content_type="application/json")


@require_http_methods(["GET"])
def get_postagem(request, postagem_id):
    """Retorna todas as postagens."""
    postagem = Postagem.objects.filter(pk=postagem_id)

    postagem_json = serializers.serialize("json", postagem)

    return HttpResponse(postagem_json, content_type="application/json")


@require_http_methods(["POST"])
def post_postagem(request):
    """Adiciona um post."""
    nova = Postagem()
    nova.texto = request.POST["texto"]
    nova.autor = get_user_model().objects.get(pk=request.POST["autor_id"])
    nova.save()
    return HttpResponse("Postagem bem sucedida")


@require_http_methods(["DELETE"])
def delete_postagem(request, postagem_id):
    post = Postagem.objects.get(pk=postagem_id)
    post.delete()

    return HttpResponse("Deletado com sucesso.")
