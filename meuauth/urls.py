from django.urls import path
from meuauth import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
]