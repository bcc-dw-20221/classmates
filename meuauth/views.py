from django.shortcuts import HttpResponse, render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import CornoProfile

# Create your views here.
def sign_in(request):
    if request.method == "POST":
        user = request.POST["user"]
        passwd = request.POST["passwd"]

        user = authenticate(request, username=user, password=passwd)

        if user:
            login(request, user)
            return HttpResponse("O login ocorreu.")
        else:
            return HttpResponse("Você não sabe de nada.")
    else:
        return render(request, "meuauth/index.html")


def perfil(request: HttpRequest, corno_id: str) -> HttpResponse:
    """Perfil de um corno."""
    return HttpResponse(f"Olá corno de ID {corno_id}")


def cadastro(request):
    nome = request.GET["nome"]
    senha = request.GET["senha"]
    tipo = request.GET["tipo"]

    novo_corno = CornoProfile()
    novo_corno.tipo = tipo

    novo_usuario = User.objects.create_user(nome, "", senha)
    novo_usuario.save()

    novo_corno.user = novo_usuario
    novo_corno.save()

    return HttpResponse("Corno salvo com sucesso! Bem vindo ao mundo dos cornos.")
