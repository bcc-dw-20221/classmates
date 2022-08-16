from django.shortcuts import HttpResponse, render
from django.contrib.auth import authenticate, login

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        user = request.POST['user']
        passwd = request.POST['passwd']

        user = authenticate(request, username=user, password=passwd)

        if user:
            login(request, user)
            return HttpResponse('O login ocorreu.')
        else:
            return HttpResponse('Você não sabe de nada.')
    else:
        return render(request, 'meuauth/index.html')