"""URL paths do bar."""
from django.urls import path

from boteco import views

urlpatterns = [
    path("add/", views.post_postagem, name="post_postagem"),
]
