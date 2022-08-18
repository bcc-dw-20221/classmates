from django.urls import path
from meuauth import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
    # https://magote.com/myauth/profile/129/
    path('profile/<corno_id>/', views.perfil, name="perfil"),
    path('signup/', views.cadastro, name='cadastro'),
]