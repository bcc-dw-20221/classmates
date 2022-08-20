"""URL paths do bar."""
from django.urls import path

from boteco import views

urlpatterns = [
    path("", views.get_postagens, name="get_postagens"),
    path("add/", views.post_postagem, name="post_postagem"),
    path("get/<postagem_id>/", views.get_postagem, name="get_postagem"),
    path("remove/<postagem_id>/", views.delete_postagem, name="delete_postagem"),
]
