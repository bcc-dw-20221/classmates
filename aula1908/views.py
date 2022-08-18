"""Views da aula do dia 19/08."""
from django.http import HttpResponse

# Create your views here.
def exemplo1(request):
    """Sempre retorna a string e o status abaixo."""
    return HttpResponse("Uma mensagem foi retornada", status=200)


def exemplo2(request, user_id):
    """Retorna a string formatada mas o status 404"""
    return HttpResponse(f"Usuario de ID: {user_id} nao existe.", status=404)
