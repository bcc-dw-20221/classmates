from django.urls import path

from aula1908 import views

urlpatterns = [
    path("exemplo1/", views.exemplo1, name="exemplo1"),
    path("exemplo2/<user_id>/", views.exemplo2, name="exemplo2"),
]
