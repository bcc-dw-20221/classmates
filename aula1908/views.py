from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def exemplo1(request):
    return HttpResponse("Uma mensagem foi retornada", status=200)


def exemplo2(request, user_id):
    return HttpResponse(f"Usuario de ID: {user_id} nao existe.", status=404)
