"""Views do bar."""

# Create your views here.
from django.shortcuts import HttpResponse


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
