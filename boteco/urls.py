"""URL paths do bar."""
from django.urls import path, include
from rest_framework import routers

from boteco import views
from boteco.viewsets import (
    PerfilViewSet,
    UserViewSet,
    BebidaViewSet,
    TipoDeCornoViewSet,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"perfis", PerfilViewSet)
router.register(r"bebidas", BebidaViewSet)
router.register(r"tipos", TipoDeCornoViewSet)

urlpatterns = [
    path("", views.get_postagens, name="get_postagens"),
    path("add/", views.post_postagem, name="post_postagem"),
    path("get/<postagem_id>/", views.get_postagem, name="get_postagem"),
    path(
        "remove/<postagem_id>/", views.delete_postagem, name="delete_postagem"
    ),
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
