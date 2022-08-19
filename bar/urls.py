"""URL paths do bar."""
from django.urls import path

from bar import views

urlpatterns = [
    path('add/', views.post_postagem, name="post_postagem"),
]
